# Import tkinter module
import tkinter as tk
import threading
from time import sleep
from random import randint
from tkinter import messagebox

# Create window object
window = tk.Tk()
window.title('Draw')
# Window size
window.minsize(800, 600)
# Put the student's name in the list
name_list = ['Classmate 1', 'Classmate 2', 'Classmate 3', 'Classmate 4', 'Classmate 5', 'Classmate 6',
             'Classmate 7', 'Classmate 8', 'Classmate 9', 'Classmate 10', 'Classmate 11', 'Classmate 12',
             'Classmate 13', 'Classmate 14', 'Classmate 15', 'Classmate 16', 'Classmate 17', 'Classmate 18']
# Create an empty list to place the finished button
btn_list = []
# Loop through the length of the student list
for i in range(len(name_list)):
	# Set the button, pass in the student's name as the text displayed on the button, set the font, and set the button color to white
    button = tk.Button(window, text=name_list[i], font=('SimSun 15 bold'), bg='white')
    # Add the button to the button list
    btn_list.append(button)
    # Press the row placement button. Since 6 rows are placed in each row, the quotient and remainder of 6 are taken.
    # Can be changed according to the number of buttons placed in each row
    y, x = divmod(i, 6)
    # Place the button, the position will change according to the value of i
    button.place(x=100+x*100, y=100+y*100, width=80, height=80)


def round():
    # After clicking the button, judge the text displayed by the button, and then change to the opposite
    if btn_start['text'] == 'Start':
        btn_start['text'] = 'stop'
    else:
    	# If the text displayed is ‘stop’ when the button is clicked, the function will jump out.
        btn_start['text'] = 'Start'
        return
    # Set the length of the button list, which is the number of students
    m = len(btn_list)
    # Randomly generate the value of i, i will be used as the index value of the button list
    # That is, it will start randomly when you click the start button
    i = randint(0, m-1)
    while True:
        # Iterate over all the buttons and change the background of all components to white
        for x in btn_list:
            x['bg'] = 'white'
        # Set the background color of the component corresponding to the current value to red, indicating the selected state
        btn_list[i]['bg'] = 'red'
        # Determine whether the text displayed on the button is ‘start’,
        # Because only when the stop button is clicked, the displayed text will become ‘start’, a popup will appear, and the loop will jump out
        if btn_start['text'] == 'Start':
        	# Set the pop-up window and use the showinfo function to display the winning information
            tk.messagebox.showinfo('Winning', message='Congratulations to becoming a lucky one'.format(btn_list[i]['text']))
            # Create a new window to achieve the effect of pop-up window, you can set the font size and window size
            # If necessary, you can use this part of the code
            # popup = tk.Tk()
            # popup.title('Winning')
            # text ='Congratulations {} to be lucky'. format(btn_list[i]['text'])
            # msg = tk.Label(popup, text=text, font=('SimSun 15 bold'), width=30, height=5)
            # # Layout function pack
            # msg.pack(side=tk.LEFT)
            # popup.mainloop()
            break
        # Reassign i to a random coordinate, the purpose is to make the button randomly selected every time when drawing
        i = randint(0, m-1)
        # Delay, you can change the time control speed
        sleep(0.05)


# Create thread function
def newtask():
    # Create a thread and run it, target is passed into the function to start the lottery
    t = threading.Thread(target=round)
    t.start()


# Set the start button, commond passes in the function executed when the button is clicked
btn_start = tk.Button(window, text='Start', font=('SimSun 15 bold'), command=newtask)
# Place the start button
btn_start.place(x=300, y=450, width=200, height=80)
# Event loop, keep the window not closed
window.mainloop()