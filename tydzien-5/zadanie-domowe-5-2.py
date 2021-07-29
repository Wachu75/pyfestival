'''
pytaj u. o nazwy produktów tak długo aż nie napisze koniec
zapisz do pliku o nazwie ddmmrrrr.txt tylko unikatowe nazwy
'''
import pendulum

dt = pendulum.now()

def save_file(data, file_name):
    with open(file_name, 'a') as handler:
        handler.write(data)

def take_data():
    temp = dt.format('DDMMYYYY', locale='pl') # jak chcesz mieć np godzineminutedate.txt użyj = dt.format('hmDDMMYYYY', locale='pl')
    file = ""+ temp + ".txt"
    print(file)
    return file


words = set()

necessary_condition = True

while necessary_condition:
    word_in = str(input("podaj nazwę produktu lub koniec:  "))
    if word_in == "koniec":
        necessary_condition = False
        words = str(words)
        save_file(words, take_data())
        continue

    words.add(word_in)

    print(words)

