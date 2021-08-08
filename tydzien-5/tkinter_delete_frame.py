'''
When you press button then you can destroy() this frame to remove all widgets and you can run the
same function to create widgets again. Or you can run different function to create different frame with widgets
- so you can replace content in window.
BTW: if you do var = Widget().pack() then you assign None to var and you have no access to Widget
- ie. you can't detroy it. You have to do it in two steps

var = Widget()
var.pack()

if you don't need access to widget then you don't need variable

Widget().pack()

And when you have access to all widgets then you can change settings (ie. clear text) in every widget instead of
destroying all widgets.
'''
from tkinter import *

# --- functions ---

def create_frame(master):
    print("create frame")

    frame = Frame(master)

    b = Button(frame, text='Do Something')
    b.pack(pady=10)

    clearall = Button(frame, text='reset', command=reset_all)
    clearall.pack(pady=10)

    return frame

def reset_all():
    global frame

    frame.destroy()
    frame = create_frame(master)
    #frame = create_different_frame(master)
    frame.pack()

# --- main ---


master = Tk()

frame = create_frame(master)
frame.pack()

mainloop()