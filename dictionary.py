'''
słowniki tworzymy urzywając nawiasó { }
lub dict()

'''

products = {
    'cos_a': 3.5,
    'cos_b': 10,
    'cos': 1.4,
    '1': ('one', 'jeden')

}
print(list(products.values()))
print('-' * 50)
print(products.keys())
print(' ')

for product in products:
    print(product)
    print(products[product])

print('-' * 30)

for name, price in products.items():
    print(f'nazwa {name} \t \t cena {price}')

product = input('co podac? ')
if product not in products:
    print('tego nie ma ')
    quit()

price = products[product]
quantity = int(input('należy podać ilosc: '))

print(f'cena {price * quantity}')

#temporary.update({0:'a'}) aktualizuje wartość wg klucza
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.update({"model": "White"})
# print(car)

from collections import defaultdict

items = ["1", "2", "a", "g", "g"]
backpack = defaultdict(int) # urzycie defaultdict umorzliwia literowanie po słowniku bez ryzyka błędu w indeksie
for item in items:
    backpack[item] += 1


