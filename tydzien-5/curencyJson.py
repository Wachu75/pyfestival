import urllib
from json import loads
import urllib.request

with urllib.request.urlopen('http://api.nbp.pl/api/exchangerates/tables/A/') as site:
    data = loads(site.read().decode('utf-8'))
    rates = data[0]['rates']
    exchange = input('jaka wartosc: ')
    value, code = exchange.split(' ')
    value = float(value)
    rate = list(filter(lambda x: x['code'] == code, rates))
    print(value * rate[0]["mid"])



