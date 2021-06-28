import tkinter as tk

root = tk.Tk()
root.geometry('480x480')

tk.Label(root, text='Login').grid(row=0, column=0, padx=50, pady=10)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text='Password').grid(row=7, column=0)
tk.Entry(root).grid(row=7,column=1)

tk.mainloop()