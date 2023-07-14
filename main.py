from tkinter import *
from tkinter import ttk
import functions as f


root = Tk()
root.title("PassGen")
root.geometry("400x400+500+100")
root.resizable(False, False)
root.iconbitmap("icon.ico")


btn = ttk.Button(root, text="Generate")
btn.pack()

label = ttk.Label(text="Hello Tkinter", background="#FFCDD2", foreground="#B71C1C", padding=8)
label.pack(expand=True)
mainloop()