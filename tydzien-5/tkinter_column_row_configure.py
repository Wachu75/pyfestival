import tkinter as tk
from tkinter import *


class spam1():
    def __init__(self, root):
        self.root = root
        self.create_buttons()
        self.create_rest_of_layout()

    def create_buttons(self):
        # Configure root window for rows and cols according to "ideal result"
        self.root.rowconfigure([0, 1, 2], weight=1)
        self.root.columnconfigure([0, 1], weight=1)
        card_frame = Frame(self.root)
        card_frame.grid(row=0, column=0, sticky=N + S + E + W)

        # Configure 5 rows and 10 columns
        card_frame.rowconfigure([0, 1, 2, 3, 4], weight=1)
        card_frame.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weight=1)

        # Create a 5x10 (rows x columns) grid of buttons inside the frame
        i = 0
        for row_index in range(5):
            for col_index in range(10):
                # Set card image
                card_image = PhotoImage(file='beer.png')
                small_card_image = card_image.subsample(2, 2)
                # Create button
                btn = Button(card_frame,
                             width=5, height=5,
                             image=small_card_image,
                             bg="azure",
                             borderwidth=0,
                             command=lambda i=i: self.card_button_clicked(i))
                btn.image = small_card_image
                btn.grid(row=row_index, column=col_index, sticky=N + S + E + W)
                i = i + 1

    def card_button_clicked(self, x):
        print(x)

    def create_rest_of_layout(self):
        # Create the rest of the frames
        a = Label(self.root, text='middle', bg='tan')
        a.grid(row=1, column=0, sticky=N + S + E + W)
        b = Label(self.root, text='bottom', bg='khaki')
        b.grid(row=2, column=0, sticky=N + S + E + W)
        c = Label(self.root, text='top right', bg='bisque')
        c.grid(rowspan=2, row=0, column=1, sticky=N + S + E + W)
        d = Label(self.root, text='bottom right', bg='gold')
        d.grid(row=2, column=1, sticky=N + S + E + W)


root = tk.Tk()

spam1(root)

root.mainloop()
