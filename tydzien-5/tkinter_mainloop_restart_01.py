import tkinter as tk
from tkinter import Button, Entry, Canvas, Label, ttk
import concurrent.futures


class Application(tk.Frame):
    def __init__(self, master=None):
        self.master = master

    def Create_canvas(self, canvas_width, canvas_height):
        global canvas  # described as global because used outside class
        canvas = tk.Canvas(master, bg='papaya whip', width=canvas_width, height=canvas_height)

    def Application_Intro(self):
        print("starting new app")
        restart_program_button = tk.Button(canvas, text="Restart_program", font='Helvetica 12 bold', width=20, height=2,
                                           command=self.Restart)
        start_program_button = tk.Button(canvas, text="Start_program", font='Helvetica 12 bold', width=20, height=2,
                                         command=self.Start_program)
        canvas.create_text(960, 20, text="MY PROGRAM", font='Helvetica 16 bold')
        canvas.create_window(710, 300, window=restart_program_button)
        canvas.create_window(710, 500, window=start_program_button)
        canvas.pack()
        master.mainloop()

    def Start_program(self):
        global restart
        print("Program start,checking if restart is required")
        if (restart == 1):
            print("GOING BACK TO IDLE STATE")
            restart = 0
            return
        else:
            master.after(1000, self.Start_program)

    def Restart(self):  # IF TASK STARTED SET RESTART =1, IF NOT restart devices and refresh app
        global restart
        restart = 1
        print("HERE I WANT TO INTERRUPT START PROGRAM AND RETURN TO IDLE STATE")
        print("REFRESH GUI ELEMENTS, DESTROY ANY WIDGETS IF CREATED")
        print("RESET THE GLOBAL VARIABLE VALUES")

        # master.mainloop()
        # WHAT TO DO IN THIS FUNCTION TO GO BACK TO INITIAL MAINLOOP STATE??
        return


def main():
    global restart
    restart = 0


main()
master = tk.Tk()
app = Application(master=master)
app.Create_canvas(1920, 1080)

app.Application_Intro()