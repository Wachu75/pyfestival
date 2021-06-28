'''
listy możemy modyfikować !
list[2] = x spowoduje zapisanie w list pod indeksem 2 wartość x
listy mogą mieć dowolne typy w liście ale przyjmuje się że są to dane tego samego typy !
do zamiany na liste urzywamy list(typ...)
jeżeli nie dajemy nawiasów [ ] domyślnie definuijemy tuple !!!
przy list musimy zawsze podać nawiasy [ ...,...]


'''
list1 = [] # tworzymy pustą listę którą możemy np: uzupełnić wartościami urzywając list1.append(value)
fruits = ['owoc', 'aple', 'lemon', 'aple'] #musimu! podać nawiasy kwaratowe ponieważ nie podanie domyslnie definiuje tuple a to jest lista
list(fruits) # do rzutowania na liste
tuple(fruits) # do tzutowania na tuple
word = 'samuraj'
a = list(word)
print(a)
b = tuple(word)
print(b)
# listy są mutowalne i kolejność jest zachowana
fruits.append('orange')
print(fruits)
fruits.remove('aple')
print(fruits)
del fruits[1]
print(fruits)

