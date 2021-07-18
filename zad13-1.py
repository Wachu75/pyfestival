a = set()
b = set()
d = set()

for i in range(1, 1000):
    if i % 5 == 0:
        a.add(i)
    if i % 3 == 0:
        b.add(i)
    if i % 3 == 0 and i % 5 == 0:
        d.add(i)

c = set(range(0, 1000, 6))
print(sorted(a))
print(sorted(c))

print(sorted(a & b))
print(sorted(d))
