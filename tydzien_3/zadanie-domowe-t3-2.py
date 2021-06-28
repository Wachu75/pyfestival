value = int(input('podaj liczbę do policzenia silni : '))
values = 1
while value > 1:
    values *= value
    value -= 1
print(values)

#----------------------------------------------
# rozwiazanie Kacpra

def get_factorial(number: int) -> int:
    factorian = 1
    while number > 0:
        factorian *= number
        number -=1
    return  factorian

print(get_factorial(3))
print(get_factorial(0))
print(get_factorial(1))

