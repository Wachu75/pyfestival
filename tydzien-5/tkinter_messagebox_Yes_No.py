'''

'''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

# create the root window
root = tk.Tk()
root.title('Tkinter Yes/No Dialog')
root.geometry('300x150')

# click event handler
def confirm():
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to quit?')
    if answer:
        root.destroy()


ttk.Button(
    root,
    text='Ask Yes/No',
    command=confirm).pack(expand=True)


# start the app
root.mainloop()

''' using object-oriented programing

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, askquestion


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Yes/No Dialog')
        self.geometry('300x150')

        # Quit button
        quit_button = ttk.Button(self, text='Quit', command=self.confirm)
        quit_button.pack(expand=True)

    def confirm(self):
        answer = askyesno(title='Confirmation',
                          message='Are you sure that you want to quit?')
        if answer:
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
'''