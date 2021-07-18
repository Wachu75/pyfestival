products = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6
}


for a, b in products.items():
    print(f'nazwa:  {a} \t\t\t cena:  {b}')

pod = {}

for a in range(65, 91):
    #leter = (chr(a))
    pod[chr(a)] = a
# print(pod)
print("{" + "\n\t" + "\n\t".join("{!s} :\t{!r} ,".format(v, k) for k, v in pod.items()) + "\n" + "}")


lower = [70, 79, 88, 97, 106, 115]
upper = [78, 87, 96, 105, 114, 12345]
num = [5, 3, 4, 2, 6, 4]
digits = len(str(max(lower + upper)))
print(digits)

f = '{0:>%d}-{1:>%d}: {3} {2}' % (digits, digits) #digits liczy dlugosc max w lower upper w tym przypadku 3
# {3} odnosi się do linijki niżej i jest to ostatni argument x w f.format(..., ..., ..., 'x')
for i in range(len(num)):
    #print(int(i))
    print(f.format(lower[i], upper[i], '*' * num[i], 'x'))

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use ">" to right-align the value:

txt = "We have {:>8} chickens."
print(txt.format(49))
txt1 = "{0}-{1}-{2}-{3}"
print(txt1.format(2 , 3 , 4 , 5))

txt = "Mi casa, su cata. costa"

x = txt.rindex("casa")
y = len("casa")
print(x)
print(y)


print(txt[x:x+y])

txt = "Hello, welcome to my world."

if txt.rfind("q") == -1:
    print("nothing found")

#print(txt.rindex("q")) throw error!
