#Dokończ poprzednią pracę domową.. zamianę liczb dziesiętnych na binarne
#za pomocą pętli while :)

# 10 / 2 = 5 reszta 0
# 5 / 2 = 4 r 1
# 4 / 2 = 2 r 0
# 2 / 2 = 1 jeden przepisujemy

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


