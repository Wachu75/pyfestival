import tkinter as tk


class TestGrid(tk.Frame):
    def __init__(self, master, switch):
        tk.Frame.__init__(self, master, bg='white')
        colors = ['cyan', 'magenta', 'green', 'gold', 'lavender', 'purple']
        self.switch = switch

        self.widgets = []
        for i in range(6):
            self.widgets.append(tk.Label(self, text=i, bg=colors[i]))

    def draw(self):
        for w in self.widgets:
            w.grid_forget()

        positions = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]
        for i in range(6):
            c, r = positions[i][0], positions[i][1]
            if self.switch:
                c, r = r, c
            self.grid_columnconfigure(c, weight=1, uniform="aaa")
            self.grid_rowconfigure(r, weight=1, uniform="bbb")
            self.widgets[i].grid(column=c, row=r, sticky=tk.NSEW)


class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('400x400+20+20')

        btn = tk.Button(self, text="click me")
        btn.pack(side=tk.TOP, fill=tk.X)
        btn.bind("<Button-1>", self.transpose)

        self.switch = False
        self.frm = None
        self.create_frm()

    def create_frm(self):
        self.frm = TestGrid(self, self.switch)
        self.frm.draw()
        self.frm.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

    def transpose(self, *args):
        self.frm.destroy()
        self.switch = not self.switch
        self.create_frm()


def main():
    root = MyApp()
    root.mainloop()


if __name__ == '__main__':
    main()