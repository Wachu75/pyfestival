from tkinter import *
from random import *


w = Tk()

def random_colour():
    hex_char = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code = '#'
    for i in range(0,6):
        colour_code = colour_code + choice(hex_char)
    return colour_code
def random_colour_1():
    return f'#{randint(0,0xffffff):06x}'

#
# colour_code = colour_code + choice(hex_char)
# colour_code = colour_code + choice(hex_char)
# colour_code = colour_code + choice(hex_char)
# colour_code = colour_code + choice(hex_char)
# colour_code = colour_code + choice(hex_char)

#print(colour_code)
my_canvas1 = Canvas(w,width=500,height=500,bg="white")
#my_canvas2 = Canvas(w,width=100,height=100,bg="orange")
my_canvas1.create_line(0,0,300,400,fill='black',width=20)
my_canvas1.create_oval(250,250,100,100,fill=random_colour(),width=20)
#print(help(Canvas))
my_canvas1.grid(row=0, column=0)
#my_canvas2.grid(row=0, column=1)
for i in range(0,500):
    x1=randint(0,500)
    x2=randint(0,500)
    y1=randint(0,500)
    y2=randint(0,500)
    random_wight=randint(1,10)
    my_canvas1.create_line(x1,x2,y1,y2,width=random_wight,fill=random_colour_1())
    my_canvas1.update()

my_canvas1.delete('all')

my_canvas1.create_line(10,30,490,30,fill='blue',arrow='last',width=4)
my_canvas1.create_line(10,100,490,100,fill='blue',arrow='last',arrowshape=(64,80,24),width=4)
my_canvas1.create_line(10,180,490,180,fill='blue',arrow='last',arrowshape=(80,80,24),width=4)

my_canvas1.delete('all')

def display_coordinates(event):
    my_label['text']=f'x={event.x} y={event.y}'
    
my_canvas1.bind('<Button-1>',display_coordinates)

my_label=Label(bd=4, relief="solid")
my_label.grid(row=1,column=0)


w.mainloop()