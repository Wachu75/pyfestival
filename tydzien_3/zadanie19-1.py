def samogloska(w):
    wynik = []
    for i, _ in enumerate(w):
        if w[i] in samogloski:
            wynik.append(w[i])
    return wynik

word = str(input('podaj słowo: '))

samogloski = [
    'a','e','i','o','u','ą','ę','ó','y'
]

print(samogloska(word))

#wersja Kacpra

def filter_volwels(word):
    return {char for char in word if char in 'aeiouy'}

print(filter_volwels(word))



