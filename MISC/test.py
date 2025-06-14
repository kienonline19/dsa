import tkinter as tk


def encode_ceasar_cipher():
    key = k.get()
    string = txt_inp.get("1.0", "end-1c")

    ans = []

    for ch in string:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            shifted = chr((ord(ch) - start + key) % 26 + start)
            ans.append(shifted)
        else:
            ans.append(ch)

    lbl_enc.config(text = ''.join(ans))


def decode_ceasar_cipher():
    key = k.get()
    string = txt_inp.get("1.0", "end-1c")

    ans = []

    for ch in string:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            shifted = chr((ord(ch) - start - key) % 26 + start)
            ans.append(shifted)
        else:
            ans.append(ch)

    lbl_dec.config(text = ''.join(ans))


root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 600
window_height = 400

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"600x400+{x}+{y}")

tk.Label(root, text = "Input string:").pack()

txt_inp = tk.Text(root, width = 40, height = 5)
txt_inp.pack(fill = tk.BOTH, expand = True, padx = 10)

k = tk.IntVar()

tk.Spinbox(root, from_ = 1, to = 25, textvariable = k).pack()

button_frame = tk.Frame(root)
button_frame.pack(pady = 10)

tk.Button(button_frame, text = "Encode", command = encode_ceasar_cipher).pack(side = tk.LEFT, padx = 5)
tk.Button(button_frame, text = "Decode", command = decode_ceasar_cipher).pack(side = tk.LEFT, padx = 5)

lbl_enc = tk.Label(root)
lbl_enc.pack()
lbl_dec = tk.Label(root)
lbl_dec.pack()

root.mainloop()
