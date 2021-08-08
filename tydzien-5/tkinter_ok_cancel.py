import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING

# create the root window
root = tk.Tk()
root.title('Tkinter Ok/Cancel Dialog')
root.geometry('300x150')

# click event handler


def confirm():
    answer = askokcancel(
        title='Confirmation',
        message='Deleting will delete all the data.',
        icon=WARNING)

    if answer:
        showinfo(
            title='Deletion Status',
            message='The data is deleted successfully')


ttk.Button(
    root,
    text='Delete All',
    command=confirm).pack(expand=True)


# start the app
root.mainloop()

''' example object-oriented programing

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Ok/Cancel Dialog')
        self.geometry('300x150')

        delete_button = ttk.Button(
            self,
            text='Delete All',
            command=self.confirm)

        delete_button.pack(expand=True)

    def confirm(self):
        answer = askokcancel(
            title='Confirmation',
            message='Deleting will delete all the data.',
            icon=WARNING)

        if answer:
            showinfo(
                title='Deletion Status',
                message='The data is deleted successfully')


if __name__ == "__main__":
    app = App()
    app.mainloop()
'''