import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as messagebox

def vigenere_cipher(text, key, encrypt=True):
    result = ''
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A') if key_char.isupper() else ord(key_char) - ord('a')
            if encrypt:
                result += chr((ord(char) + shift - ord('A')) % 26 + ord('A')) if char.isupper() else chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            else:
                result += chr((ord(char) - shift - ord('A')) % 26 + ord('A')) if char.isupper() else chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            result += char
    return result

class VigenereApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vigenere Cipher")
        self.root.geometry("400x300")

        self.text_label = ctk.CTkLabel(root, text="Enter Text:")
        self.text_label.pack(pady=10)

        self.text_entry = ctk.CTkEntry(root, width=100)
        self.text_entry.pack(pady=10)

        self.key_label = ctk.CTkLabel(root, text="Enter Key:")
        self.key_label.pack(pady=10)

        self.key_entry = ctk.CTkEntry(root, width=100)
        self.key_entry.pack(pady=10)

        self.encrypt_button = ctk.CTkButton(root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = ctk.CTkButton(root, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack(pady=10)

    def show_result_popup(self, result):
        popup = ctk.CTkToplevel(self.root)
        popup.title("Result")
        popup.geometry("300x200")

        result_text = ScrolledText(popup, wrap=ctk.WORD, width=30, height=10)
        result_text.insert(ctk.END, result)
        result_text.pack(pady=10)

        copy_button = ctk.CTkButton(popup, text="Copy", command=lambda: self.copy_to_clipboard(result))
        copy_button.pack(pady=10)

    def copy_to_clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()

    def encrypt_text(self):
        text = self.text_entry.get()
        key = self.key_entry.get()
        if text and key:
            encrypted_text = vigenere_cipher(text, key, encrypt=True)
            self.show_result_popup(encrypted_text)
        else:
            messagebox.showwarning("Error", "Please enter both text and key.")

    def decrypt_text(self):
        text = self.text_entry.get()
        key = self.key_entry.get()
        if text and key:
            decrypted_text = vigenere_cipher(text, key, encrypt=False)
            self.show_result_popup(decrypted_text)
        else:
            messagebox.showwarning("Error", "Please enter both text and key.")

if __name__ == "__main__":
    ctk.set_appearance_mode("System") # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue") # Themes: blue (default), dark-blue, green
    root = ctk.CTk()
    app = VigenereApp(root)
    root.mainloop()