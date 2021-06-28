
# https://restcountries.eu/rest/v2/name/Polska

from json  import loads
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

country = input('Podaj kraj: ')
try:
    with urlopen(f'https://restcountries.eu/rest/v2/name/{country}') as response:
        data = loads(response.read().decode('utf-8'))
        country_data = data[0]
        print(country_data['capital'])
except (URLError, HTTPError) as error:
    print('błąd: ', error)
