import tkinter as tk


class A:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Aeronics Consultoria Pvt. Ltd.")
        self.window.geometry('500x500')
        self.window.configure(background='black')
        self.label = tk.Label(self.window)


a = A()
