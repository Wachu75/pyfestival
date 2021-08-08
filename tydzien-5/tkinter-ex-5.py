import tkinter as tk
from tkinter import messagebox
from functools import partial

buttonClicked = False

def callback(args):
    # if args == 'ok':
    print(args)

def send_name(values):
    print(first_name.get())
    print('click')
    if first_name.get() != '':
        print(values)
        messagebox.showinfo(title='ok', message='witam szefa')
    else:
        print(values)
        messagebox.showerror(title='blad', message='idziesz na sciecie')

root = tk.Tk()
root.geometry('480x480')

tk.Label(root, text='Login').grid(row=0, column=0, padx=50, pady=20)
first_name = tk.Entry(root)  #.grid(row=0, column=1)
first_name.grid(row=0, column=1)
tk.Label(root, text='Password').grid(row=15, column=0)
tk.Entry(root).grid(row=15,column=1)


button = tk.Button(text="OK", command= partial(callback, 'Ą')) # command=lambda :callback('ok'))
button.grid(row=30, column = 1)
#button.pack()

tk.mainloop()