import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()
root.geometry('920x600+270+50')
root.minsize(960, 600)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
Attendance_frame = tk.Frame(root)
Attendance_frame.grid(row=0, column=0, sticky='nsew')

attendaceBox = tk.LabelFrame(Attendance_frame,
                             text='Take Attendance',
                             bd=4,
                             relief='groove',
                             labelanchor='n',
                             font='Arial 10 bold',
                             fg='navy blue',
                             width=850,
                             height=525)
attendaceBox.grid(row=0, column=0, sticky='nsew', padx=15)

Attendance_frame.columnconfigure(0, weight=1)
Attendance_frame.rowconfigure(0,weight=1)

dateFrame = tk.Frame(attendaceBox)  # A small frame to accommodate date entry label & entry box
dateFrame.grid(row=0, column=0, sticky='nsew')

font = 'TkDefaultFont 10 bold'
date_label = tk.Label(dateFrame, text='Enter Date : ', font=font)
date_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)

date_entry = DateEntry(dateFrame, date_pattern='dd/mm/yyyy', showweeknumbers=False, showothermonthdays=False)
date_entry.grid(row=0, column=1, sticky='w')

noteLabel = tk.Label(attendaceBox, text='Note: Uncheck the boxes for absentees', anchor='w')
noteLabel.grid(row=1, column=0, sticky='nsew')

attendaceBox.rowconfigure(2, weight=1)
canvas = tk.Canvas(attendaceBox, width=200, borderwidth=0, background="#ffffff")
# You can set width of canvas according to your need
canvas.grid(row=2, column=0, sticky='nsew')
canvas.columnconfigure(0, weight=1)
canvas.rowconfigure(0, weight=1)
vsb = tk.Scrollbar(attendaceBox, orient="vertical", command=canvas.yview)
vsb.grid(row=2, column=1, sticky='nsew')
canvas.configure(yscrollcommand=vsb.set)

checkFrame = tk.Frame(canvas, bg='green')
canvas.create_window((0, 0), window=checkFrame, anchor="nw", tags='expand')
checkFrame.columnconfigure(0, weight=1)



for i in range(0, 51):  # A loop to create Labels of students roll numbers & names
    c = tk.Checkbutton(checkFrame, anchor='w', text=f"{'2018-MC-' + str(i + 1)}       Student {i + 1}")
    c.grid(row=i, column=0, sticky='nsew')
    c.select()
canvas.bind('<Configure>', lambda event: canvas.itemconfigure('expand', width=event.width))
checkFrame.update_idletasks()
canvas.config(scrollregion=canvas.bbox('all'))


root.mainloop()