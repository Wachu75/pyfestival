from tkinter import *

class RedFrame(Frame):
    def __init__(self, the_window):
        super().__init__()
        self["height"]=150
        self["width"]=150
        self["relief"]=RAISED
        self["bd"]=8
        self["bg"]="red"
    def rel(self,a):
        self['relief']=SUNKEN
    def rel1(self,b):
        self['relief']=RAISED


w = Tk()

frame1 = RedFrame(w)
frame2 = Frame(w)
print(help(Frame))

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)

print('type id of frame1 is ', id(frame1))
print('the type of frame1 is', type(frame1))


w.mainloop()