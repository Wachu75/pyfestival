#Dokończ poprzednią pracę domową.. zamianę liczb dziesiętnych na binarne
#za pomocą pętli while :)


def decimalToBinary(value):
    binary = []
    while value != 1:
        rest = value % 2
        temp = int(value / 2)
        value = temp
        binary.append(rest)
    binary.append(value)
    return binary[::-1]

print(decimalToBinary(15))
print(decimalToBinary(5))
print(decimalToBinary(9))


