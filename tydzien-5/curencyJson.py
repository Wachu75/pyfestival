import urllib
from json import loads
import urllib.request

with urllib.request.urlopen('http://api.nbp.pl/api/exchangerates/tables/A/') as site:
    data = loads(site.read().decode('utf-8'))  # decode powoduje że możemy pracować jak na tekscie
    rates = data[0]['rates']
    print(rates)
    #exchange = input('podaj jaką wartosc: i skrót waluty: (USD)')
    value = input('podaj jaką wartosc chcesz wymienić: ')
    code = input('podaj skrót waluty którą chcesz wymnienić: ') # exchange.split(' ')
    value = float(value)
    rate = list(filter(lambda x: x['code'] == code, rates))
    # lambda zwróci wartość tylko wtedy gdy wartość x['code'] będzie równa wartości code i chcemy to wykonać
    #  na naszych wszystich pobranych walutach czyli rates
    # [{'currency': 'dolar..', 'code': 'USD', 'mid': 3.8851}] takie coś jest po rate
    # teraz musimy odwołać się do listy rate[0] ponieważ tylko jeden element listy otrzymaliśmy urzywamy indexu[0]
    # i z listy z klucza 'mid' pobieramy wartość człość przypisujemy do rate po filtrowaniu i rzuceniu na liste
    #
    print(rate)
    print(rate[0]["code"]) # wyświetli np USD jeżeli takie podaliśmy ponieważ pod kluczem code jest ....
    print(rate[0]["mid"])  # wyświetli wartość spod klucza 'mid'
    print(value * rate[0]["mid"])



