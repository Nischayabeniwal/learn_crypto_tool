# Caesar Cipher - Encrypt and Decrypt Text with Tkinter GUI
# Author: Nischaya

import tkinter as tk
from tkinter import ttk, messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def process():
    mode = mode_var.get()
    message = message_entry.get()
    try:
        shift = int(shift_entry.get())
        if not (0 <= shift <= 25):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer between 0 and 25.")
        return

    if mode == "Encrypt":
        result = encrypt(message, shift)
        output = f"Encrypted Message:\n{result}"
    else:
        result = decrypt(message, shift)
        output = f"Decrypted Message:\n{result}"

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, output)
    result_text.config(state="disabled")

def clear_fields():
    message_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.config(state="disabled")

# Tkinter GUI setup
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("420x260")
root.resizable(False, False)

mainframe = ttk.Frame(root, padding="15 15 15 15")
mainframe.grid(row=0, column=0, sticky="NSEW")

title_label = ttk.Label(mainframe, text="Caesar Cipher Tool", font=("Segoe UI", 16, "bold"), foreground="#2a4d69")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

ttk.Label(mainframe, text="Message:", font=("Segoe UI", 11)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
message_entry = ttk.Entry(mainframe, width=40, font=("Segoe UI", 10))
message_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

ttk.Label(mainframe, text="Shift (0-25):", font=("Segoe UI", 11)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
shift_entry = ttk.Entry(mainframe, width=5, font=("Segoe UI", 10))
shift_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

mode_var = tk.StringVar(value="Encrypt")
mode_frame = ttk.Frame(mainframe)
mode_frame.grid(row=3, column=1, sticky="w", pady=5)
ttk.Radiobutton(mode_frame, text="Encrypt", variable=mode_var, value="Encrypt").pack(side="left", padx=2)
ttk.Radiobutton(mode_frame, text="Decrypt", variable=mode_var, value="Decrypt").pack(side="left", padx=2)

button_frame = ttk.Frame(mainframe)
button_frame.grid(row=4, column=0, columnspan=2, pady=10)
ttk.Button(button_frame, text="Process", command=process).pack(side="left", padx=10)
ttk.Button(button_frame, text="Clear", command=clear_fields).pack(side="left", padx=10)

result_text = tk.Text(mainframe, height=4, width=45, font=("Segoe UI", 11), foreground="#41729f", background="#f0f4f8", borderwidth=2, relief="groove", wrap="word")
result_text.grid(row=5, column=0, columnspan=2, padx=5, pady=10)
result_text.config(state="disabled")

root.mainloop()
