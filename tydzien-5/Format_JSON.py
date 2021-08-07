from json import load, loads, dump, dumps

# 's' na końcu oznacza string bez 's' oznacz plik
# load  plik.json => listy/słowniki  jeżeli odczytujemy plik.json
# loads string.json => listy/słowniki
# dump  listy/słowniki => zapisuje plik.json
# dumps lista/słowniki => zapisuje do stringa


# struktura podobna do list i słowników
# "KLUCZE" muszą być w apostrofach
# służy do przenoszenia danych pomiędzy systemami np: przez API
'''
{
    "id": 1,
    "name": "pystart",
    "members": [
        {
            "id": 1,
            "first_name": "jan",
            "last_name": "Kowalski"
        },{
            "id": 2,
            "first_name": "olek",
            "last_name": "Nowak"
        }
        ]
    
    
}
'''