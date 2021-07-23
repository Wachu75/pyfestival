def euklides_while(a: int, b: int) ->int:
    while b != 0:
        c = a % b
        a = b # inny zapis operacji przypisania a, b = b, c rozwiązanie Kacpra
        b = c
    return a


def euklides_if(a: int, b: int) ->int:     # z tym miałem duży problem ;-(
    if a == 0:
        return b
    return euklides_if(b % a, a)


def euklides_recursion(a: int, b: int) ->int:
    pass
# tak właściwie to moje euklides_if jest rozwiązaniem Kacpra jako rekurencja :-)

# def test_euklides_while():
#     assert euklides_while(8, 4) == 4
#     assert euklides_while(27, 36) == 9


print('wynik while:', euklides_while(8, 4))
print('wynik if:', euklides_if(8, 4))
print('wynik while:', euklides_while(15, 36))
print('wynik if:', euklides_if(15, 36))
print('wynik while:', euklides_while(9, 27))
print('wynik if:', euklides_if(9, 27))

