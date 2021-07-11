iloczyn = 1
value = 1
while value != 'koniec':
    value = input('podaj liczbę lub koniec')
    if value != 'koniec':
        iloczyn *= int(value) if int(value) % 2 == 0 else 1

print(iloczyn)

# inne rozwiazanie
#done = False
# while not done:
#     value = input('podaj liczbę lub koniec')
#     if value == 'koniec':
#         done = True
#         continue
#     elif int(value) % 2 == 0:
#         iloczyn *= int(value)
#print(iloczyn)