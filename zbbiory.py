#do deklaracji możemy użyć nawisów {} tyle, że nie urzywamy : lecz ,
#do rzutowania na zbiór używany set()
#brak kolejności
#tylko wartości unikatowe
#
zb_3 = set()
zb_5 = set()
for i in range(3,1001,3):
    zb_3.add(i)
for i in range(5,1001,5):
    zb_5.add(i)
# gamoniu zapamiętaj pętle w python to ostateczność !!!
zb_4 = set(range(4,1001,4)) # tworzymy zbior tak jak wyżel
zb_6 = set(range(6,1001,6))
print(
    sorted(
        list(zb_6)
    )
)

wspolna = zb_3 & zb_5

print(sorted(wspolna))

word1 = set('abcdef')
word2 = set('efghij')
name1 = 'Krzysztof'
name2 = 'Bartek'
print(set(name1.lower()) ^ set(name2.lower()))


word = word1 | word2
print(word)

word = word1 ^ word2
print(word)

word = word1 & word2
print(word)

word = word1 - word2
print(word)

baza = set()
for _ in range(10):
    baza.add(input('podaj adres e-mail:'))

print(baza)

