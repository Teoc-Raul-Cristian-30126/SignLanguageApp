import tkinter as tk
from tkinter import messagebox

import requests
import json


class LoginFrame:
    url = 'http://localhost:8081/user/login'

    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(self.root, padx=20, pady=20)

        self.labelEmail = None
        self.labelPassword = None

        self.entryEmail = None
        self.entryPassword = None

        self.buttonCreateAccount = None
        self.buttonLogin = None

        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for email
        self.labelEmail = tk.Label(self.frame, text="Email:")
        self.labelEmail.grid(row=0, column=0, pady=5)
        self.entryEmail = tk.Entry(self.frame)
        self.entryEmail.grid(row=0, column=1, pady=5)

        # Label and Entry for password
        self.labelPassword = tk.Label(self.frame, text="Password:")
        self.labelPassword.grid(row=1, column=0, pady=5)
        self.entryPassword = tk.Entry(self.frame, show="*")
        self.entryPassword.grid(row=1, column=1, pady=5)

        # Login button
        self.buttonLogin = tk.Button(self.frame, text="Login", command=self.verify_login)
        self.buttonLogin.grid(row=2, column=0, pady=10)

        # Go to RegisterFrame button
        self.buttonCreateAccount = tk.Button(self.frame, text="Create Account", command=self.app.show_register_frame)
        self.buttonCreateAccount.grid(row=2, column=1, pady=10)

    def verify_login(self):
        email = self.entryEmail.get()
        password = self.entryPassword.get()

        # Check user
        myObj = {
            "email": email,
            "password": password
        }

        x = requests.get(self.url, json=myObj)

        if x.status_code == 200:
            messagebox.showinfo("Login Success", "Login Successful!")
            self.app.show_main_frame()
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")

        # Delete text after verify
        self.entryEmail.delete(0, tk.END)
        self.entryPassword.delete(0, tk.END)

    def pack(self):
        self.frame.pack(pady=10)

    def unpack(self):
        self.frame.pack_forget()
