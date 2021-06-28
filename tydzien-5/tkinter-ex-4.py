import tkinter

def on_frame_click(e):
    print("frame clicked")

def on_button_click(e):
    print('button')

tk = tkinter.Tk()
a_frame = tkinter.Frame(tk, bg="red", padx=20, pady=20)
a_label = tkinter.Label(a_frame, text="A Label")
a_botton = tkinter.Button(a_frame, text='BOTTON')#, command=on_frame_click())
a_frame.pack()
a_label.pack()
a_botton.pack()
a_botton.bind("<Button>", on_button_click)
tk.protocol("WM_DELETE_WINDOW", tk.destroy)
a_frame.bind("<Button>", on_frame_click)
tk.mainloop()
#
# b2.bind('<Button-3>', funkcjaPrzycisku2)
# b2.bind('<Button-1>', funkcjaPrzycisku3)
# b2.place(x=50, y=150)
#
# root.bind('<Button-3>', funkcjaOkna)