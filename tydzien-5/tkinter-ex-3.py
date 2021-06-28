import tkinter as tk


class TestGrid(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg='white')
        colors = ['cyan', 'magenta', 'green', 'gold', 'lavender', 'purple']
        self.switch = True
        self.widgets = []
        for i in range(6):
            self.widgets.append(tk.Label(self, text=i, bg=colors[i]))

    def refresh(self, *args):
        self.switch = not self.switch
        for w in self.widgets:
            w.grid_forget()

        positions = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]
        for i in range(6):
            c, r = positions[i][0], positions[i][1]
            if self.switch:
                c, r = r, c
            self.widgets[i].grid(column=c, row=r, sticky=tk.NSEW)
        for i in range(2):
            # set the weight for the always present columns and rows
            self.grid_columnconfigure(i, weight=1, uniform="aaa")
            self.grid_rowconfigure(i, weight=1, uniform="bbb")
        if self.switch:
            # tell grid manager to give no weight to the empty column
            self.grid_columnconfigure(2, weight=0, uniform="ignore")
            self.grid_rowconfigure(2, weight=1, uniform="bbb")
        else:
            # tell grid manager to give no weight to the empty row
            self.grid_columnconfigure(2, weight=1, uniform="aaa")
            self.grid_rowconfigure(2, weight=0, uniform="ignore")


def main():
    root = tk.Tk()
    root.geometry('400x400+20+20')
    btn = tk.Button(root, text="click me")
    btn.pack(side=tk.TOP, fill=tk.X)
    frm = TestGrid(root)
    frm.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
    frm.refresh()
    btn.bind("<Button-1>", frm.refresh)

    root.mainloop()

if __name__ == '__main__':
    main()