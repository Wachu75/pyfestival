done = False
iloczyn = 1
# while not done:
#     value = input('podaj liczbę lub koniec')
#     if value == 'koniec':
#         done = True
#         continue
#     elif int(value) % 2 == 0:
#         iloczyn *= int(value)
print(iloczyn)
value = 1
while value != 'koniec':
    value = input('podaj liczbę lub koniec')
    iloczyn *= int(value) if int(value) % 2 == 0 else 1

print(iloczyn)
