import tkinter as tk

root = tk.Tk()

def myfunction(*args):
    x = var.get()
    y = stringvar1.get()
    z = stringvar2.get()
    if x and y and z:
        button.config(state='normal')
    else:
        button.config(state='disabled')

stringvar1 = tk.StringVar(root)
stringvar2 = tk.StringVar(root)
var = tk.StringVar(root)

stringvar1.trace("w", myfunction)
stringvar2.trace("w", myfunction)
var.trace("w", myfunction)

entry1 = tk.Entry(root, width=15, textvariable=stringvar1)
entry1.grid(row=1,column=1)
entry2 = tk.Entry(root, width=15, textvariable=stringvar2)
entry2.grid(row=1,column=2)

choices = ('a','b','c')
option = tk.OptionMenu(root, var, *choices)
option.grid(row=1,column=3)

button = tk.Button(root,text="submit")
button.grid(row=1, column=4)

root.mainloop()