import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

ENCRYPTION_KEY = 4  # Fixed encryption number


def encrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + ENCRYPTION_KEY) % 26 + start)
        else:
            result += char
    return result[::-1]


def decrypt(text):
    text = text[::-1]
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - ENCRYPTION_KEY) % 26 + start)
        else:
            result += char
    return result


class SecureFileGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Encrypted File System")
        self.root.geometry("500x550")

        tk.Label(root, text="Secure Encrypted File System", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Button(root, text="Create Secure File", width=30, command=self.create_window).pack(pady=10)
        tk.Button(root, text="Open Secure File", width=30, command=self.open_window).pack(pady=10)

    def create_window(self):
        win = tk.Toplevel(self.root)
        win.title("Create Secure File")
        win.geometry("500x550")

        tk.Label(win, text="Filename").pack()
        filename_entry = tk.Entry(win, width=40)
        filename_entry.pack()

        tk.Label(win, text="Normal Password").pack()
        normal_entry = tk.Entry(win, show="*", width=40)
        normal_entry.pack()

        tk.Label(win, text="Secret Password").pack()
        secret_entry = tk.Entry(win, show="*", width=40)
        secret_entry.pack()

        tk.Label(win, text="Enter File Content").pack(pady=5)
        content_box = scrolledtext.ScrolledText(win, width=50, height=10)
        content_box.pack()

        def save_file():
            filename = filename_entry.get().strip()
            normal = normal_entry.get().strip()
            secret = secret_entry.get().strip()
            content = content_box.get("1.0", tk.END).strip()

            if not filename or not normal or not secret or not content:
                messagebox.showerror("Error", "All fields are required")
                return

            encrypted_content = encrypt(content)

            with open(filename, "w") as f:
                f.write(normal + "\n")
                f.write(secret + "\n")
                f.write(encrypted_content)

            messagebox.showinfo("Success", "File created and encrypted successfully")
            win.destroy()

        tk.Button(win, text="Create File", command=save_file).pack(pady=10)

    def open_window(self):
        win = tk.Toplevel(self.root)
        win.title("Open Secure File")
        win.geometry("500x550")

        tk.Label(win, text="Filename").pack()
        filename_entry = tk.Entry(win, width=40)
        filename_entry.pack()

        tk.Label(win, text="Password").pack()
        password_entry = tk.Entry(win, show="*", width=40)
        password_entry.pack()

        output_box = scrolledtext.ScrolledText(win, width=50, height=15)
        output_box.pack(pady=10)

        def open_file():
            filename = filename_entry.get().strip()
            password = password_entry.get().strip()

            if not os.path.exists(filename):
                messagebox.showerror("Error", "File does not exist")
                return

            with open(filename, "r") as f:
                normal = f.readline().strip()
                secret = f.readline().strip()
                encrypted_content = f.read()

            output_box.delete("1.0", tk.END)

            if password == normal:
                output_box.insert(tk.END, "ENCRYPTED CONTENT:\n\n" + encrypted_content)
            elif password == secret:
                output_box.insert(tk.END, "DECRYPTED CONTENT:\n\n" + decrypt(encrypted_content))
            else:
                messagebox.showerror("Access Denied", "Incorrect password")

        tk.Button(win, text="Open File", command=open_file).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = SecureFileGUI(root)
    root.mainloop()
