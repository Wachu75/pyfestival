
def euklides_while(a: int, b: int) ->int:
    while b != 0:
        c = a % b
        a,b = b,c
    return a


def euklides_if(a: int, b: int) ->int:
    if b == 0:
        return a

    return euklides_while(b, a % b)


def test_euklides_while():
    assert euklides_while(8, 4) == 4
    assert euklides_while(27, 36) == 9


print(euklides_while(8,4))
print(euklides_if(15,36))
