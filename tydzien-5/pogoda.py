from urllib.request import urlopen
from json import loads

URL = 'https://danepubliczne.imgw.pl/api/data/synop/'

with urlopen(URL) as file:
    data = loads(file.read().decode('utf-8'))
    print(data)
    print(data[1]['stacja'])
    city = input('podaj miasto')

    info = [row for row in data if row['stacja'] == city]
    if len(info) == 0:
        print('nie wiem')
    else:
        temperatura = info[0]['temperatura']
        presure = info[0]['cisnienie']

        print(f'{temperatura}   {presure}')