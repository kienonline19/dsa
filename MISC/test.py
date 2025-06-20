import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

FONT_FAMILY = ("Helvetica", 12)


def add_text(data):
    txt_output.delete("1.0", tk.END)
    txt_output.insert("1.0", data)


def encode_ceasar_cipher():
    try:
        key = int(key_spb.get())
        string = txt_inp.get("1.0", "end-1c")

        ans = []

        for ch in string:
            if ch.isalpha():
                start = ord('A') if ch.isupper() else ord('a')
                shifted = chr((ord(ch) - start + key) % 26 + start)
                ans.append(shifted)
            else:
                ans.append(ch)

        add_text(''.join(ans))
    except Exception as e:
        msg.showerror("Error", str(e))


def decode_ceasar_cipher(key):
    try:
        string = txt_inp.get("1.0", "end-1c")

        ans = []

        for ch in string:
            if ch.isalpha():
                start = ord('A') if ch.isupper() else ord('a')
                shifted = chr((ord(ch) - start - int(key)) % 26 + start)
                ans.append(shifted)
            else:
                ans.append(ch)

        result = ''.join(ans)
        add_text(result)
        return result
    except Exception as e:
        msg.showerror("Error", str(e))


def brute_force():
    top = tk.Toplevel(root)
    top.title("Crack Ceasar Cipher")
    top.geometry("600x600")

    txt_bf = tk.Text(top, font=FONT_FAMILY)
    txt_bf.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    decs = [
        f"Key {key:02d} => " + decode_ceasar_cipher(key)
        for key in range(26)
    ]

    txt_bf.insert("1.0", '\n'.join(decs))

    top.mainloop()


root = tk.Tk()

root.title("Ceasar Cipher")
root.iconbitmap("cipher.ico")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 600
window_height = 400

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"600x400+{x}+{y}")

lbl_inp_frame = tk.LabelFrame(root, text="Input")
lbl_inp_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

txt_inp = tk.Text(lbl_inp_frame, width=40, height=5, font=FONT_FAMILY)
txt_inp.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

lbl_key_frame = tk.LabelFrame(root, text="Key")
lbl_key_frame.pack()
key_spb = ttk.Spinbox(lbl_key_frame, from_=1, to=25)
key_spb.pack(padx=5, pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Encode",
           command=encode_ceasar_cipher).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Decode", command=lambda: decode_ceasar_cipher(
    key_spb.get())).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Brute Force",
           command=brute_force).pack(side=tk.LEFT, padx=5)

lbl_out_frame = tk.LabelFrame(root, text="Output")
lbl_out_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
txt_output = tk.Text(lbl_out_frame, width=40, height=5, font=FONT_FAMILY)
txt_output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

root.mainloop()
