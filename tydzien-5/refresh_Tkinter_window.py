'''
The simplest way is to implement the entire window as a subclass of a tk Frame,
and then destroy and recreate it. Your code might look something like this:
Though,there's nothing really magical about subclassing Frame. You just need to have a function
that creates a frame and puts a bunch of widgets in it. When you want to refresh,
just delete the frame and call your function again. Using a class is a bit more convenient,
 but a class isn't strictly necessary
'''

import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        '''<other code here...>'''

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.frame = None
        refreshButton = tk.Button(self.root, text="refresh", command=self.refresh)
        self.refresh()

    def refresh(self):
        if self.frame is not None:
            self.frame.destroy()
        self.frame = Example(self.root)
        self.frame.grid(...)