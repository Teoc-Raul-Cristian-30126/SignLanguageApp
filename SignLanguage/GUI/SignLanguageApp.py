import tkinter as tk
from tkinter import messagebox

from LoginFrame import *
from RegisterFrame import *
from MainFrame import *


class SignLanguageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Language Recognition Application")

        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window
        self.root.geometry(f'+{position_right}+{position_top}')

        self.loginFrame = LoginFrame(self.root, self)
        self.registerFrame = RegisterFrame(self.root, self)
        self.mainFrame = MainFrame(self.root, self)

        self.show_login_frame()

    def show_login_frame(self):
        self.registerFrame.unpack()
        self.mainFrame.unpack()
        self.loginFrame.pack()

    def show_register_frame(self):
        self.loginFrame.unpack()
        self.registerFrame.pack()

    def show_main_frame(self):
        self.loginFrame.unpack()
        self.mainFrame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = SignLanguageApp(root)
    root.mainloop()
