names = 'cytr', 'dedaed', 'dsadsa'
b = (1, )
a = tuple(range(1,21))
print(type(a))
print(type(b))
print(sorted(a, reverse=True))
print(a[18:])
x = list(names)
x.append('trelefelemorele')
print(x)
print(type(x))
b = sum(a[18:])

print(b)
a, b, _ = names
print(names)
print(type(names))
print(a)
print(b)
print(_)
print('cytr' in names)

print(a.upper())
