'''
if os.path.isfile(file): .... funkcja sprawdza czy plik o nazie file istnieje
else:
  file istnieje
lines = list(map(lambda line: line.strip(), f)) - f = open(file, 'r', encoding)
print(*lines,sep=' ')  *lines jest rownoznaczny z zapisem print(lines[0], lines[1] .....
handler = open('test.txt')  handler to zmienna do której zapisujemy wynik open.txt
line = handler.readline()   line jest zmienną do której przypisujemy wykonanie obiektu readline
print(line)
handler.close()

kontekst menager jak skończy się wcięcie with to plik zamknie się samoczynnie !!!
with open('text.txt', 'r') as handler:
    r tylko odczyt r+ odczyt i zapis, wsaznik na początku
    w tylko zapis, plik jest czyszczony
    w+ zapis i odczyt, plik jest czyszczony
    a zapis i wskaznik ustawia na końcu

    line = handler.readline() # pozwala odczytać 1 linie
    line = handler.readlines() # pobiera cały plik linie zamieniane są na liste, każda linia zamieniana jest na element lisy
    print(line)
    po opuszczeniu with zamknięcie następuje samoczynnie !!!

def open(file, mode='r', buffering=None, encoding=None, )
    file nazwa pliku, mode co będziemy robić

with open('text.txt', 'r') as handler: #r jest domyślnie więc można go pominąć
    for line in handler:
        print(line.strip()) # strip usuwa wszystkie znaki nie drukowane puste enter na koncu każdej lini i każdy pusty znak

with open('text.txt', 'a') as file
    file.write('pierwsza linia\n')
with open('text.txt', 'a') as file
    file.write('druga linia\n')
with open('text.txt', 'a') as file
    file.write('trzecia linia\n')  # z atrybutem 'a' będzie dopisywać kolejne linie w nowych liniach do tego samego pliku

handler.write('cos tam') zapisuje do pliku przy atybucie 'a'
handler.writeline( ) zapisuje wiele lini na raz ?

import pickle
lista = [10,20,'trzydziesci',[1,2]]         typ list
with open('plik.pickle','wb') as output:    taka nazwa pliku:plik.pickle może być .txt
pickle.dump(lista,output)                   co i gdzie chce zdumpować
output.close()

with open('plik.pickle','rb') as input:
unpickle=pickle.load(input)
print(unpickle,type(unpickle))

rozwiązanie to umożliwia dokładne odtworzenie tego co chcemy zachować czyli w efekcie uzyskamy lista = [10,20,'trzydziesci',[1,2]]
typu list !!!

problem: jeżeli zmieniliśmy obiekt(klasę) to wczytanie może się nie udać:
chodzi o sytuację, gdy zapisany obiekt klasy i obecna klasa (pola,metody) różnią się
'''