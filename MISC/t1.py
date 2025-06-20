import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, messagebox
from tkinter import simpledialog
import itertools
import threading
import time
import queue

FONT_FAMILY = ("Arial", 12)


def _vigenere_cipher(text, key, mode):
    result = []
    key = key.upper()
    key_len = len(key)
    key_as_int = [ord(char) - ord('A') for char in key]

    j = 0
    for char in text:
        if 'A' <= char.upper() <= 'Z':
            is_upper = char.isupper()
            char_offset = ord('A') if is_upper else ord('a')

            char_val = ord(char.upper()) - ord('A')

            if mode == 1:
                shifted_val = (char_val + key_as_int[j % key_len]) % 26
            else:
                shifted_val = (char_val - key_as_int[j % key_len] + 26) % 26

            result.append(chr(shifted_val + char_offset))
            j += 1
        else:
            result.append(char)
    return "".join(result)


def encrypt_text():
    text = txt_inp.get("1.0", tk.END).strip()
    key_val = k.get().strip()

    if not text or not key_val:
        messagebox.showwarning("ERROR", "Please enter both text and key!")
        return

    encrypted_text = _vigenere_cipher(text, key_val, 1)
    txt_output.delete("1.0", tk.END)
    txt_output.insert(tk.END, encrypted_text)
    status_var.set(f"Text encrypted with key: {key_val}")


def decrypt_text():
    text = txt_inp.get("1.0", tk.END).strip()
    key_val = k.get().strip()

    if not text or not key_val:
        messagebox.showwarning("ERROR", "Please enter both text and key!")
        return

    decrypted_text = _vigenere_cipher(text, key_val, -1)
    txt_output.delete("1.0", tk.END)
    txt_output.insert(tk.END, decrypted_text)
    status_var.set(f"Text decrypted with key: {key_val}")


class BruteForceWorker:
    """Worker class to handle brute force operations in a separate thread."""

    def __init__(self, cipher_text, max_key_length, result_queue, progress_queue):
        self.cipher_text = cipher_text
        self.max_key_length = max_key_length
        self.result_queue = result_queue
        self.progress_queue = progress_queue
        self.stop_event = threading.Event()
        self.total_combinations = 0
        self.current_combination = 0

        # Calculate total combinations for progress tracking
        for length in range(1, max_key_length + 1):
            self.total_combinations += 26 ** length

    def run(self):
        """Main brute force operation."""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        try:
            for key_length in range(1, self.max_key_length + 1):
                if self.stop_event.is_set():
                    break

                # Send progress update for key length
                self.progress_queue.put(
                    ('status', f"Trying key length: {key_length}..."))

                for key_chars_tuple in itertools.product(alphabet, repeat=key_length):
                    if self.stop_event.is_set():
                        break

                    current_key = "".join(key_chars_tuple)
                    decrypted_attempt = _vigenere_cipher(
                        self.cipher_text, current_key, -1)

                    # Send result
                    result_line = f"Key: '{current_key}' -> Decrypted: '{decrypted_attempt}'"
                    self.result_queue.put(
                        ('result', current_key, decrypted_attempt, result_line))

                    # Update progress
                    self.current_combination += 1
                    progress_percent = (
                        self.current_combination / self.total_combinations) * 100
                    self.progress_queue.put(('progress', progress_percent))

                    # Small delay to prevent overwhelming the GUI
                    time.sleep(0.001)

            if not self.stop_event.is_set():
                self.progress_queue.put(('complete', 'Brute force completed!'))
            else:
                self.progress_queue.put(
                    ('stopped', 'Brute force stopped by user.'))

        except Exception as e:
            self.progress_queue.put(
                ('error', f"Error during brute force: {str(e)}"))

    def stop(self):
        """Stop the brute force operation."""
        self.stop_event.set()


def brute_force_text():
    cipher_text = txt_inp.get("1.0", tk.END).strip()

    if not cipher_text:
        messagebox.showwarning("ERROR", "Please enter cipher text!")
        return

    max_key_length_str = max_len_var.get().strip()

    if not max_key_length_str:
        messagebox.showwarning("ERROR", "Please enter maximum key length!")
        return

    try:
        max_key_length = int(max_key_length_str)
        if max_key_length <= 0:
            raise ValueError
        if max_key_length > 6:  # Reasonable limit to prevent excessive computation
            if not messagebox.askyesno("Warning",
                                       f"Key length {max_key_length} will generate {sum(26**i for i in range(1, max_key_length+1))} combinations.\n"
                                       "This may take a very long time. Continue?"):
                return
    except ValueError:
        messagebox.showerror(
            "ERROR", "The maximum key length must be a positive integer.")
        return

    # Create brute force window
    create_brute_force_window(cipher_text, max_key_length)


def create_brute_force_window(cipher_text, max_key_length):
    """Create and manage the brute force results window."""
    global brute_force_worker, brute_force_thread

    brute_force_window = tk.Toplevel(root)
    brute_force_window.title("Brute Force Results")
    brute_force_window.protocol(
        "WM_DELETE_WINDOW", lambda: stop_brute_force(brute_force_window))

    # Position window
    main_window_x = root.winfo_x()
    main_window_y = root.winfo_y()
    main_window_width = root.winfo_width()
    main_window_height = root.winfo_height()

    new_window_width = 800
    new_window_height = 600
    new_window_x = main_window_x + \
        (main_window_width // 2) - (new_window_width // 2)
    new_window_y = main_window_y + \
        (main_window_height // 2) - (new_window_height // 2)
    brute_force_window.geometry(
        f"{new_window_width}x{new_window_height}+{new_window_x}+{new_window_y}")

    # Control frame
    control_frame = tk.Frame(brute_force_window)
    control_frame.pack(fill=tk.X, padx=10, pady=5)

    # Progress bar
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(
        control_frame, variable=progress_var, maximum=100, mode='determinate')
    progress_bar.pack(fill=tk.X, pady=(0, 5))

    # Status label
    status_label = tk.Label(
        control_frame, text="Initializing...", font=FONT_FAMILY)
    status_label.pack(anchor=tk.W)

    # Buttons frame
    button_frame = tk.Frame(control_frame)
    button_frame.pack(fill=tk.X, pady=5)

    stop_button = ttk.Button(button_frame, text="Stop",
                             command=lambda: stop_brute_force(brute_force_window))
    stop_button.pack(side=tk.LEFT, padx=(0, 5))

    clear_button = ttk.Button(button_frame, text="Clear Results",
                              command=lambda: clear_results(brute_force_output_text))
    clear_button.pack(side=tk.LEFT, padx=(0, 5))

    save_button = ttk.Button(button_frame, text="Save Results",
                             command=lambda: save_results(brute_force_output_text))
    save_button.pack(side=tk.LEFT)

    # Results display
    brute_force_output_text = scrolledtext.ScrolledText(
        brute_force_window, width=90, height=25, font=("Consolas", 10))
    brute_force_output_text.pack(
        fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

    # Initialize queues
    result_queue = queue.Queue()
    progress_queue = queue.Queue()

    # Create and start worker thread
    brute_force_worker = BruteForceWorker(
        cipher_text, max_key_length, result_queue, progress_queue)
    brute_force_thread = threading.Thread(
        target=brute_force_worker.run, daemon=True)
    brute_force_thread.start()

    # Start monitoring the queues
    monitor_brute_force_progress(brute_force_window, brute_force_output_text,
                                 status_label, progress_var, result_queue, progress_queue)

    brute_force_output_text.insert(tk.END, f"Starting brute force attack...\n")
    brute_force_output_text.insert(tk.END, f"Cipher text: {cipher_text}\n")
    brute_force_output_text.insert(
        tk.END, f"Maximum key length: {max_key_length}\n")
    brute_force_output_text.insert(
        tk.END, f"Total combinations to try: {sum(26**i for i in range(1, max_key_length+1))}\n\n")


def monitor_brute_force_progress(window, output_text, status_label, progress_var, result_queue, progress_queue):
    """Monitor the progress of brute force operation and update GUI."""
    try:
        # Process progress updates
        while not progress_queue.empty():
            msg_type, *data = progress_queue.get_nowait()

            if msg_type == 'status':
                status_label.config(text=data[0])
            elif msg_type == 'progress':
                progress_var.set(data[0])
            elif msg_type == 'complete':
                status_label.config(text=data[0])
                progress_var.set(100)
                output_text.insert(tk.END, f"\n{data[0]}\n")
                output_text.see(tk.END)
                return  # Stop monitoring
            elif msg_type == 'stopped':
                status_label.config(text=data[0])
                output_text.insert(tk.END, f"\n{data[0]}\n")
                output_text.see(tk.END)
                return  # Stop monitoring
            elif msg_type == 'error':
                status_label.config(text="Error occurred")
                output_text.insert(tk.END, f"\nERROR: {data[0]}\n")
                output_text.see(tk.END)
                messagebox.showerror("Error", data[0])
                return  # Stop monitoring

        # Process results
        results_processed = 0
        while not result_queue.empty() and results_processed < 10:  # Limit batch size
            msg_type, key, decrypted, result_line = result_queue.get_nowait()
            output_text.insert(tk.END, f"{result_line}\n")
            results_processed += 1

        if results_processed > 0:
            output_text.see(tk.END)

        # Schedule next update
        window.after(100, lambda: monitor_brute_force_progress(
            window, output_text, status_label, progress_var, result_queue, progress_queue))

    except Exception as e:
        print(f"Error in monitoring: {e}")
        # Continue monitoring even if there's an error
        window.after(100, lambda: monitor_brute_force_progress(
            window, output_text, status_label, progress_var, result_queue, progress_queue))


def stop_brute_force(window):
    """Stop the brute force operation."""
    global brute_force_worker
    if brute_force_worker:
        brute_force_worker.stop()
    window.destroy()


def clear_results(text_widget):
    """Clear the results text widget."""
    text_widget.delete(1.0, tk.END)


def save_results(text_widget):
    """Save results to a file."""
    from tkinter import filedialog

    filename = filedialog.asksaveasfilename(
        title="Save Results",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if filename:
        try:
            content = text_widget.get(1.0, tk.END)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            messagebox.showinfo("Success", f"Results saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {str(e)}")


def copy_to_main_output():
    """Copy selected text from input to main output."""
    try:
        selected_text = txt_inp.selection_get()
        txt_output.delete(1.0, tk.END)
        txt_output.insert(tk.END, selected_text)
        status_var.set("Text copied to output")
    except tk.TclError:
        messagebox.showinfo("Info", "Please select text first")


def clear_all():
    """Clear all text fields."""
    txt_inp.delete(1.0, tk.END)
    txt_output.delete(1.0, tk.END)
    k.set("")
    max_len_var.set("")
    status_var.set("All fields cleared")


# Global variables for thread management
brute_force_worker = None
brute_force_thread = None

# Create main window
root = tk.Tk()
root.title("Vigenère Cipher - Enhanced with Threading")

# Center window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 700
window_height = 600
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Input text frame
lbl_inp_frame = tk.LabelFrame(root, text="Input Text", font=FONT_FAMILY)
lbl_inp_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

txt_inp = scrolledtext.ScrolledText(
    lbl_inp_frame, width=40, height=6, font=FONT_FAMILY)
txt_inp.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Key and settings frame
settings_frame = tk.Frame(root)
settings_frame.pack(fill=tk.X, padx=5, pady=5)

# Key frame
lbl_key_frame = tk.LabelFrame(settings_frame, text="Key", font=FONT_FAMILY)
lbl_key_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
k = tk.StringVar()
key = ttk.Entry(lbl_key_frame, textvariable=k, font=FONT_FAMILY)
key.pack(padx=5, pady=5, fill=tk.X)

# Max length frame
lbl_max_len_frame = tk.LabelFrame(
    settings_frame, text="Max Brute Force Key Length", font=FONT_FAMILY)
lbl_max_len_frame.pack(side=tk.RIGHT, padx=(5, 0))
max_len_var = tk.StringVar()
max_len_entry = ttk.Entry(
    lbl_max_len_frame, textvariable=max_len_var, font=FONT_FAMILY, width=15)
max_len_entry.pack(padx=5, pady=5)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Encrypt",
           command=encrypt_text).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Decrypt",
           command=decrypt_text).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Brute Force",
           command=brute_force_text).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Copy Selected",
           command=copy_to_main_output).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Clear All",
           command=clear_all).pack(side=tk.LEFT, padx=5)

# Output frame
lbl_out_frame = tk.LabelFrame(root, text="Output Results", font=FONT_FAMILY)
lbl_out_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
txt_output = scrolledtext.ScrolledText(
    lbl_out_frame, width=40, height=8, font=FONT_FAMILY)
txt_output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Status bar
status_frame = tk.Frame(root)
status_frame.pack(fill=tk.X, side=tk.BOTTOM)
status_var = tk.StringVar()
status_var.set("Ready")
status_bar = tk.Label(status_frame, textvariable=status_var,
                      relief=tk.SUNKEN, anchor=tk.W, font=("Arial", 10))
status_bar.pack(fill=tk.X, padx=2, pady=2)

# Set default values
max_len_var.set("3")

root.mainloop()
