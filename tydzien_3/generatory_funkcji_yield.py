#  yield  to taki return
# pozwala na to że funkcja zwraca wielokrotnie cos
# funkcja działa w tle a program działa osobno
# dzięki generatorom funkcja może zwracać nie czekając na pełen wynik
# pozwala optymalizować pamięć potrzebną do obsłużenia naszego żądania + program działa szybciej

def get_numbers(numbers: range):
    for i in numbers:
        print(f'iteruje ... liczbe dla {i}')
        yield i + i

result = get_numbers(range(111,222))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
# robienie next jest mało efektywne tzn co zrobić jeżeli nie będziemy wiedzieli ile razy mamy go wywołać
# można inaczej tzn. po generatorach możemy iterować

def get_numbers(numbers: range):
    for i in numbers:
        print(f'iteruje ... liczbe dla {i}')
        yield i + i

for n in get_numbers(range(1,11)):
    print(f'wynik: {n}')
# efekt tego rozwiązania jest taki, że jeżeli generator z jakiegoś powodu zwolni to również zwolni pętla for ponieważ
# nie otrzyma ona od niego kolejnego wyniku.
# kolejny plus to: np. scrolując strony internetowe po znalezieniu pierwszego elementu z interesujących nas elementów
# możemy od razu przekazać go do dalszej obróbki

# generator liczb pierwszych: nie czekamy na zakończenie funkcji jeżeli się zawiesi, w tym czasie wykonujemy program dalej
# a jeżeli otrzymamy kolejną liczbę pierwszą to ją obrabiamy

from math import sqrt, floor
def is_prime(n):
    pass

def generate_prime_numbers():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

for number in generate_prime_numbers():
    print(f'to liczba pierwsza: {number}')

# a jak zatrzymać taki generator !!!
primes = generate_prime_numbers()
for number in primes:
    print(f'to liczba pierwsza: {number}')
    if len(str(number)) >=6:
        print('wystarczy kończymy działanie yield')
        primes.close()

# close() wywołane na zmiennej primes do której jest podpięty generator yield
