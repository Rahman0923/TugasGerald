import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Tk App")
        self.geometry("400x200")
        self.label = ttk.Label(self, text="Hello, Semua")
        self.label.pack(pady=20)
        ttk.Button(self, text="Click Gwe", command=self.on_click).pack()

    def on_click(self):
        self.label.config(text="Muntazier Ganteng!")


if __name__ == "__main__":
    App().mainloop()
