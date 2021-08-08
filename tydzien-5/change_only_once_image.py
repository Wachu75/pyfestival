import tkinter as tk

# --- classes ---

class MainWindow():

    def __init__(self):
        self.master = tk.Tk()

        # canvas for image
        self.canvas = tk.Canvas(self.master, width=60, height=60)
        self.canvas.pack()

        # images
        self.images = [
            tk.PhotoImage(file="ball1.gif"),
            tk.PhotoImage(file="ball2.gif"),
            tk.PhotoImage(file="ball3.gif"),
        ]
        self.current_image_number = 0

        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.images[self.current_image_number])

        # button to change image
        self.button = tk.Button(self.master, text="Change", command=self.on_click)
        self.button.pack()

        self.master.mainloop()

    def on_click(self):

        # next image
        self.current_image_number += 1

        # return to first image
        if self.current_image_number == len(self.images):
            self.current_image_number = 0

        # change image on canvas
        self.canvas.itemconfig(self.image_on_canvas, image=self.images[self.current_image_number])

# --- main ---

MainWindow()
