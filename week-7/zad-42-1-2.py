
capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin'
}


try:
    country = input('Podaj nazwę państwa: ')
    print(capitals[country])
except KeyError:
    print(f'Nie wiem jaka jest stolica: {country}')
