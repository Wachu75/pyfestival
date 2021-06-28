from tkinter import *


w = Tk()


def change_text():
    button1['text'] = 'zmiana botton'
    button1['state'] = 'disabled'


frame1 = Frame(w)
frame2 = Frame(w)

label1 = Label(frame1, text='label1')
label2 = Label(frame1, text='label2')
label3 = Label(frame1, text='label3')

label4 = Label(frame2, text='label1')
label5 = Label(frame2, text='label2')
label6 = Label(frame2, text='label3')

entry1 = Entry(frame1)
entry12 = Entry(frame1)
entry13 = Entry(frame1)

entry14 = Entry(frame2)
entry15 = Entry(frame2)
entry16 = Entry(frame2)

button1 = Button(frame1, text="button 1", command=change_text)
button2 = Button(frame2, text="button 2")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=0, column=0)
label5.grid(row=1, column=0)
label6.grid(row=2, column=0)

entry1.grid(row=0, column=1)
entry12.grid(row=1, column=1)
entry13.grid(row=2, column=1)
entry14.grid(row=0, column=1)
entry15.grid(row=1, column=1)
entry16.grid(row=2, column=1)

button1.grid(row=3, columnspan=2)
button2.grid(row=3, columnspan=2)

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)

w.mainloop()