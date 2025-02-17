import tkinter as tk
from tkinter import messagebox

import requests
import json


class RegisterFrame:
    url = 'http://localhost:8081/user/addUser'

    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(self.root, padx=20, pady=20)

        self.labelPassword = None
        self.labelEmail = None
        self.labelLastName = None
        self.labelFirstName = None

        self.entryPassword = None
        self.entryEmail = None
        self.entryLastName = None
        self.entryFirstName = None

        self.buttonBackToLogin = None
        self.buttonRegister = None

        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for FirstName
        self.labelFirstName = tk.Label(self.frame, text="FirstName:")
        self.labelFirstName.grid(row=0, column=0, pady=5)
        self.entryFirstName = tk.Entry(self.frame)
        self.entryFirstName.grid(row=0, column=1, pady=5)

        # Label and Entry for LastName
        self.labelLastName = tk.Label(self.frame, text="LastName:")
        self.labelLastName.grid(row=1, column=0, pady=5)
        self.entryLastName = tk.Entry(self.frame)
        self.entryLastName.grid(row=1, column=1, pady=5)

        # Label and Entry for email
        self.labelEmail = tk.Label(self.frame, text="Email:")
        self.labelEmail.grid(row=2, column=0, pady=5)
        self.entryEmail = tk.Entry(self.frame)
        self.entryEmail.grid(row=2, column=1, pady=5)

        # Label and Entry for password
        self.labelPassword = tk.Label(self.frame, text="Password:")
        self.labelPassword.grid(row=3, column=0, pady=5)
        self.entryPassword = tk.Entry(self.frame, show="*")
        self.entryPassword.grid(row=3, column=1, pady=5)

        # Register button
        self.buttonRegister = tk.Button(self.frame, text="Register", command=self.register_user)
        self.buttonRegister.grid(row=4, column=0, pady=10)

        # Back to LoginFrame button
        self.buttonBackToLogin = tk.Button(self.frame, text="Back to Login", command=self.app.show_login_frame)
        self.buttonBackToLogin.grid(row=4, column=1, pady=10)

    def register_user(self):
        firstName = self.entryFirstName.get()
        lastName = self.entryLastName.get()
        email = self.entryEmail.get()
        password = self.entryPassword.get()

        # Add user
        if firstName and lastName and email and password:
            myObj = {
                "firstName": firstName,
                "lastName": lastName,
                "email": email,
                "password": password
            }

            x = requests.post(self.url, json=myObj)

            if x.status_code == 200:
                messagebox.showinfo("Registration Success", f"User {email} registered successfully!")
                self.app.show_login_frame()
            else:
                messagebox.showerror("Registration Failed", "Email already exists.")
        else:
            messagebox.showerror("Registration Failed", "Please complete all the fields.")

        # Delete text after verify
        self.entryFirstName.delete(0, tk.END)
        self.entryLastName.delete(0, tk.END)
        self.entryEmail.delete(0, tk.END)
        self.entryPassword.delete(0, tk.END)

    def pack(self):
        self.frame.pack(pady=10)

    def unpack(self):
        self.frame.pack_forget()
