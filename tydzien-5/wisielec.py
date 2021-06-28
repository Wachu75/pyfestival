import tkinter as tk
from tkinter import *
from tkinter import messagebox


def funkcjaPrzycisku():
    print('graj')


def funkcjaPrzycisku1(event):
    print('next')


def funkcjaPrzycisku2(event):
    print('koniec')


def funkcjaPrzycisku3(event):
    print('prawy przycisk')


def funkcjaOkna(event):
    print('okno')


root = tk.Tk()
var_1 = tk.StringVar()

#root.geometry('480x480')
width_of_window = 400
height_of_window = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2) - (width_of_window/2)
y_coordinate = (screen_height/2) - (height_of_window/2)
root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
root.resizable(width=False, height=False)
#root.configure(width=480, height=480)
a_frame = tk.Frame(root, bg="lightgrey", padx=100, pady=100)
a_frame.pack()

l = tk.Label(a_frame, text="Wisielec\ndalsza czesc",borderwidth=1, relief="solid", height=4, font="Times 20", padx=50, anchor='nw')
#borderwidht <-> bd .. relief= raised/sunken/solid/ridge/groove/flat
#height = 1 wysokosć ramki dopasowana do 1 wysokosći fontu tzn 2 linie będą obcięte
# North / South / West / East / Center
# anchor = n -north / ne - northeast / e - east
# justify = RIGHT / LEFT / CENTER nie używając justify domyślnie jest wycentrowane
l['text']="cgange text\n zmiana"
#mozemy zmieniać dowolne pola label !!!
temp = l['font'] # mozemy zapisac zmienne label
label_1 = tk.Label(a_frame, relief="solid", textvariable=var_1)
label_1.pack()
var_1.set("HI")
l.pack()
#l.place()
# print(l.keys())
#for item in l.keys():
#    print(item, ":", l[item])
entry_1 = tk.Entry(root)
entry_1.pack()
#name_user = entry_1.get()
#print(name_user)


b = tk.Button(a_frame, text='graj', width=10, fg='red', command=funkcjaPrzycisku) #bg='lightgreen',
b.place(x=0, y=20)

b1 = tk.Button(a_frame, text='next', width=10, bg='green', fg='red') #, command=funkcjaPrzycisku1)
b1.bind('<Button-1>', funkcjaPrzycisku1)
b1.place(x=0, y=60)

b2 = tk.Button(a_frame, text='next', width=10, fg='red') #, command=funkcjaPrzycisku1)
b2.bind('<Button-3>', funkcjaPrzycisku2)
b2.bind('<Button-1>', funkcjaPrzycisku3)
b2.place(x=0, y=100)

a_frame.bind('<Button-3>', funkcjaOkna)

# glowne = tk.Menu()
# root.config(menu=glowne)
#
# filemenu = tk.Menu(glowne)
# glowne.add_cascade(label='1', menu=filemenu)
# filemenu.add_command(label='2')
# filemenu.add_separator()
# filemenu.add_command(label='3')
#
#
# edit = tk.Menu(glowne)
# glowne.add_cascade(label='1', menu=edit)
# edit.add_command(label='2')
# edit.add_separator()
# edit.add_command(label='3')
#
# podmenu = tk.Menu(edit)
# edit.add_cascade(label='1', menu=podmenu)
# podmenu.add_command(label='2')
# podmenu.add_separator()
# podmenu.add_command(label='3')


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.protocol("")

root.mainloop()