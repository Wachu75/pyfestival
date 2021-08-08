try:
    import Tkinter as tk
except:
    import tkinter as tk


class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('200x100')
        self.button = tk.Button(self.root,
                                text='Click Me',
                                command=lambda: [self.funcA(), self.funcB(), self.funcC()])
        self.button.pack()

        self.labelA = tk.Label(self.root, text="A")
        self.labelB = tk.Label(self.root, text="B")
        self.labelC = tk.Label(self.root, text="C")

        self.labelA.pack()
        self.labelB.pack()
        self.labelC.pack()

        self.root.mainloop()

    def funcA(self):
        self.labelA["text"] = "A responds"

    def funcB(self):
        self.labelB["text"] = "B responds"

    def funcC(self):
        self.labelC["text"] = "C responds"


app = Test()
