import tkinter as tk
from tkinter import messagebox


def send_name():
    print(first_name.get())
    print('click')
    if first_name.get() == 'topsecret':
        messagebox.showinfo(title='ok', message='witam szefa')
    else:
        messagebox.showerror(title='blad', message='idziesz na sciecie')

window = tk.Tk()
window.title('test')

label = tk.Label(window, text="kamień")
label.pack()

first_name = tk.Entry()
first_name.pack()

button = tk.Button(text="OK", command=send_name)
button.pack()

window.mainloop()
