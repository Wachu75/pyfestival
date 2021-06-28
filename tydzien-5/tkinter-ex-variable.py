from tkinter import *

def say_hello():
    #name_of_user = entry_1.get()
    # name_of_user = var_2.get()
    # string_to_display = "hello "+ name_of_user
    # var_1.set(string_to_display)
    var_1.set("Hello " + entry_1.get()) #var_1.set("hello "+ name_of_user)
    #display_label["text"] = var_2.get()
    display_label["text"] = str(entry_1.get())

my_window = Tk()
var_1=StringVar()
var_2=StringVar()

label_1=Label(my_window, text="enter:")
#entry_1 = Entry(my_window, textvariable=var_2)
entry_1 = Entry(my_window) #, textvariable=var_2)
button_1 = Button(my_window, text="clik", command=say_hello)
label_2 = Label(my_window, textvariable=var_1)
display_label = Label(my_window)

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
button_1.grid(row=1, column=0)
label_2.grid(row=1, column=1)
display_label.grid(row=3, column=1)
# grid(row=0, columnspan=2) bedzie pomiedzy dwoma kolumnami na środku

entry_1.focus()

my_window.mainloop()
