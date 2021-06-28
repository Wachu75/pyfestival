

print('Wybierz co chcesz zrobić ?')
n = input('N-nowa zbiórka, Q-wyjście z progrmau: ')

while (n == 'N' or n == 'n'):
    kwota_zbierana = 0
    ile_miesiecy = 0
    kwota = float(input('podaj kwotę którą chcesz uzbierać:'))
    while kwota_zbierana < kwota:
        suma = float(input('podaj ile możesz odłożyć miesięcznie na Twój wymarzony cel:'))
        kwota_zbierana += suma
        ile_miesiecy += 1
    print(f'Musisz oszczędzać {ile_miesiecy} miesięcy na Twój cel')
    print('\nWybierz co chcesz zrobić ?')
    n = input('N-nowa zbiórka, Q-wyjście z progrmau: ')

if (n == 'Q' or n == 'q'):
    exit()

