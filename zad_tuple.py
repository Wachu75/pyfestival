a = tuple(range(12,1025,6))
b = len(a)
print(b)
ile = 0
for zak in a:
    ile += 1
print(ile)
print(a)
print(a[:3])
print(a[-2])
print(a[3::6])
print(sorted(a[::3], reverse=True))  # lub a[::-3] // spowoduje od końca do poczatku  tuple(reverse(a) lub  a[::-1]
ostatnie_dziesiec = sum(a[-10:]) #/ len(a[-10:])
print(ostatnie_dziesiec)

print(' \n') # pusta linia

