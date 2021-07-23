
def euklides_while(a: int, b: int) ->int:
    while b != 0:
        c = a % b
        a, b = b, c
    return a


def euklides_if(a: int, b: int) ->int:
    if a == 0:
        return b
    return euklides_if(b % a, a)



# def test_euklides_while():
#     assert euklides_while(8, 4) == 4
#     assert euklides_while(27, 36) == 9


print('wynik while:', euklides_while(8, 4))
print('wynik if:', euklides_if(8, 4))
print('wynik while:', euklides_while(15, 36))
print('wynik if:', euklides_if(15, 36))

