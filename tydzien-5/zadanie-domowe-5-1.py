import tkinter as tk
from tkinter import messagebox, NSEW, E, NE, SE, S, N, NW, W, SW
from functools import partial
from PIL.ImageTk import PhotoImage, Image

canvas_width = 800
canvas_height = 600
mistake = 0
pasword = "HASŁO DO ODGADNIĘCIA"
end = ['w', 'i', 's', 'i', 'e', 'l', 'e', 'c', '', '', '', '']
hiden_pasword = ""
pasword1 = ""
end1 = []
corectly_anser = 0
foto = "img1/" + str(mistake) + ".jpg"


def hide_pasword_for_guesses(pasword):
    global hiden_pasword
    for i in range(len(pasword)):
        if pasword[i] != ' ':
            hiden_pasword += "-"
        else:
            hiden_pasword += " "
    return hiden_pasword


def send_mesage(arg):
    # TAK WIEM !!! NIE POWINIENEM ODWOłYWAć SIE DO GLOBALNYCH
    global corectly_anser
    global mistake
    global end
    global hiden_pasword
    global end1
    global pasword1
    if arg in pasword:
        for i in range(len(pasword)):
            if pasword[i] == arg:
                pasword1[i] = arg
                corectly_anser += 1
        label.config(text=" ".join(pasword1))  # text=" ".join.... prawidłowo wyświetla spacje brak .join wyświetla  { }
    if corectly_anser == len(pasword.replace(' ', '')):
        messagebox.showinfo(title='Wygrałeś', message='GRATULUJE ODBADŁEŚ HASŁO')
        img.paste(Image.open("img1/0.jpg"))
        canvas.create_image(550, 180, image=img)
        mistake = 0
        hiden_pasword = ""
        end1 = []
        corectly_anser = 0
        pasword1 = hide_pasword_for_guesses(pasword)
        pasword1 = list(pasword1)
        label.config(text=" ".join(pasword1))
    if arg not in pasword:
        mistake += 1
        end1.append(end[mistake - 1])
        foto = "img1/" + str(mistake) + ".jpg"
        img.paste(Image.open(foto))
        canvas.create_image(550, 180, image=img)
        if mistake >= 12:
            # label2.config(text=end)
            messagebox.showerror(title='Przegrałeś boś trąba', message='Będziesz wisiał!')
            img.paste(Image.open("img1/0.jpg"))
            canvas.create_image(550, 180, image=img)
            mistake = 0
            hiden_pasword = ""
            end1 = []
            corectly_anser = 0
            pasword1 = hide_pasword_for_guesses(pasword)
            pasword1 = list(pasword1)
            label.config(text=" ".join(pasword1))

large_font = ('Verdana', 30)
root = tk.Tk()
root.resizable(False, False)
root.geometry('800x600')
root.columnconfigure(0, weight=1)  # Which column should expand with window
root.rowconfigure(0, weight=1)  # Which row should expand with window
root.title("GRA WISIELEC")

canvas = tk.Canvas(root, bg='#404040', width=canvas_width, height=canvas_height)  # To see where canvas is
canvas.grid(sticky=E)
label1 = tk.Label(canvas, text="Zgadnij hasło", fg="white", bg="#404040")
label1.pack()
label1.config(font=("Courier", 30))
canvas.create_window(400, 550, window=label1)
pasword1 = hide_pasword_for_guesses(pasword)
pasword1 = list(pasword1)
label = tk.Label(canvas, text=" ".join(pasword1), fg='#404040')
label.pack()
label.config(font=("courier", 20))
canvas.create_window(canvas_width / 2, 430, window=label)
label2 = tk.Label(canvas, text=" ", bg='#404040')
label2.pack()
label2.config(font=("courier", 20))
canvas.create_window(canvas_width / 2, 380, window=label2)
img = Image.open(foto)
img = PhotoImage(img)
canvas.create_image(550, 180, image=img)

alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŻŹ"
y = 0
x = 0
for i in range(len(alfabet)):
    text = str(alfabet[i])
    widget = tk.Button(root, text=text, command=partial(send_mesage, text))
    widget.config(font=("Courier", 20))
    canvas.create_window(50 + 45 * x, 50 + 40 * y, height=35, width=35, window=widget)
    x += 1
    if (x + 1) % 6 == 0:
        y += 1
        x = 0


tk.mainloop()
