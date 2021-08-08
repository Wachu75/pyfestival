''' problem
class StartPage(tk.Frame):

def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    startLabel = tk.Label(self,
                          text="Start page")
    startLabel.pack(side="top")

    quitGroup = tk.Frame(self)
    quitGroup.pack(side="bottom")
    quitButton = tk.Button(quitGroup, text="Quit",
                           command=quit,
                           bg="pink")
    quitButton.grid(pady=10)

    channelGroup = tk.Frame(self)
    channelGroup.pack(side=tk.LEFT)
    chLabel = tk.Label(channelGroup,
                       text="Channel group")
    chLabel.grid(pady=10)

    ch1Button = tk.Button(channelGroup, text="CH1 Settings",
                          command=lambda: controller.show_frame("CH1"))
    ch1Button.grid(row=1, column=0)

    ch2Button = tk.Button(channelGroup, text="CH2 Settings",
                          command=lambda: controller.show_frame("CH2"))
    ch2Button.grid(row=2, column=0)

    ch3Button = tk.Button(channelGroup, text="CH3 Settings",
                          command=lambda: controller.show_frame("CH3"))

    ch3Button.grid(row=3, column=0)

    ch4Button = tk.Button(channelGroup, text="CH4 Settings",
                          command=lambda: controller.show_frame("CH4"))
    ch4Button.grid(row=4, column=0)

    triggerGroup = tk.Frame(self)
    triggerGroup.pack(side=tk.LEFT)
    trigLabel = tk.Label(triggerGroup,
                          text="Trigger group")
    trigLabel.grid(pady=10)
    trigButton = tk.Button(triggerGroup, text="Trigger Settings",
                           command=lambda: controller.show_frame("Trigger"))
    trigButton.grid(row=1, column=0)
    trigButton.grid(ipady=43)#43? What?

    horizGroup = tk.Frame(self)
    horizGroup.pack(side=tk.LEFT)
    horizLabel = tk.Label(horizGroup,
                          text="Horizontal group")
    horizLabel.grid(pady=10)
    horizButton = tk.Button(horizGroup,
                            text="Horizontal settings",
                            command=lambda: controller.show_frame("Horizontal"))
    horizButton.grid(row=1, column=0)
    horizButton.grid(ipady=43)#you again ...


'''

# solution problem
# import tkinter as tk
#
# root = tk.Tk()
#
# chLabel = tk.Label(root, text="Channel group")
# channelButtons = tk.Frame(root, bg='yellow')
# ch1Button = tk.Button(channelButtons, text="CH1 Settings")
# ch1Button.pack(fill='x')
# ch2Button = tk.Button(channelButtons, text="CH2 Settings")
# ch2Button.pack(fill='x')
# ch3Button = tk.Button(channelButtons, text="CH3 Settings")
# ch3Button.pack(fill='x')
# ch4Button = tk.Button(channelButtons, text="CH4 Settings")
# ch4Button.pack(fill='x')
#
# trigLabel = tk.Label(root, text="Trigger group")
# trigButton = tk.Button(root, text="Trigger Settings")
#
# horizLabel = tk.Label(root, text="Horizontal group")
# horizButton = tk.Button(root, text="Horizontal settings")
#
# # Align the labels and buttons in a 2-by-3 grid
# chLabel.grid(row=0, column=0, pady=10)
# trigLabel.grid(row=0, column=1, pady=10)
# horizLabel.grid(row=0, column=2, pady=10)
# channelButtons.grid(row=1, column=0, sticky='news')
# trigButton.grid(row=1, column=1, sticky='news')
# horizButton.grid(row=1, column=2, sticky='news')
#
# root.mainloop()