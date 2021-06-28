from math import sqrt

def isqrt(n):
    if n < 0:
        return False
    else:
        root = sqrt(n)
        if int(root + 0.5) ** 2 == n:
            return True
        else:
            return False


for i in range(0,37):
    print(i)
    print(isqrt(i))

print(isqrt(-4))
print(isqrt(-3))
print(isqrt(-2))
print(isqrt(-1))

