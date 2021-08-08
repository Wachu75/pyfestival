import pendulum

dt = pendulum.now()

def save_file(data, file_name):
    with open(file_name, 'w') as handler:
        handler.write(data)

def take_data():
    temp = dt.format('DDMMYYYYhm', locale='pl') # jak chcesz mieć np godzineminutedate.txt użyj = dt.format('hmDDMMYYYY', locale='pl')
    file = ""+ temp + ".txt"
    print(file)
    return file


words = set()

necessary_condition = True

while necessary_condition:
    word_in = str(input("podaj nazwę cos do wpisania do pliku:  "))
    if word_in == "q":
        necessary_condition = False
        words = str(words)
        save_file(words, take_data())
        continue

    words.add(word_in)

    print(words)
