import tkinter as tk
from tkinter import messagebox
from random import randint
from math import fabs



def gess_number():
    guesses.append(abs(target-int(guess.get())))
    diff = abs(target - int(guess.get()))
    if diff == 1:
        tip.configure(text='to samo')
        return
    guesses.append(diff)

    if guesses[-1] > guesses[-2]:
        tip.configure(text='zimno')

    if guesses[-1] < guesses[-2]:
        tip.configure(text='cieplej')

    if guesses[-1] == guesses[-2]:
        tip.configure(text=f'zgadles {len(guesses)}')



target = randint(1, 10)
print(target)
guesses = []

window = tk.Tk()
window.geometry('500x600')
window.title(target)

label = tk.Label(text="ZGADNIJ LICZBĘ", width=30, height=10)
label.pack()

guess = tk.Entry()
guess.pack()

button = tk.Button(text="Zgaduję", width=10, height=3, bg="blue", fg="red", command=gess_number)
button.pack()

tip = tk.Label(window, text='---------------')
tip.pack()

window.mainloop()
