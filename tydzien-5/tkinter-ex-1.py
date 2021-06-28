import tkinter as tk
root = tk.Tk()
lst = tk.Listbox(root,selectmode=tk.EXTENDED)
lst.pack()
lst.insert("end", "one", "two", "three", "four", "five")

def clickOnly(event):
    index = '@%s,%s' % (event.x, event.y)
    event.widget.focus_set()
    event.widget.select_clear(0, "end")
    event.widget.select_set(index)
    event.widget.activate(index)
    event.widget.select_anchor(index)
    return "break"

lst.bind('<Any-ButtonPress-1>', clickOnly)


tk.mainloop()