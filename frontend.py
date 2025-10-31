#abandoned tkinter GUI code

from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("300x200") 

frm = ttk.Frame(root, padding=50)
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0, pady=10)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1, pady=10)

# Center everything inside the window
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)

root.mainloop()