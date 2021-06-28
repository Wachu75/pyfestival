# ang_pol = {
#     'home': 'dom',
#     'dog': 'pies',
#     'cat': 'kot'
# }
# pol_ang = {}
#
# for ang, pol in ang_pol.items():
#     pol_ang[pol] = ang
#
# # for key, value in pol_ang.items():
# #     print(f' {key}   {value}')
# #
# #
# # for key, value in ang_pol.items():
# #     print(f' {key}   {value}')
#
# question = input('co robisz? ang-pol[1] pol-ang[2] ')
# if question not in ['1', '2']:
#     print('nie rozumiem spróbuj ponownie')
#     quit()
#
# if question == 1:
#     word = input('napisz słowo:')
#     if word not in ang_pol:
#         print('nie ma takiego słwoa w słowniku')
#         quit()
#     print(f' {ang_pol[word]}')
# else:
#     word = input('napisz słowo po polsku')
#     if word not in pol_ang:
#         print('nie znalazlem')
#         quit()
#     print(f' {pol_ang[word]}')

print(' ')

longstring = input('podaj napis:')
longstring2 = longstring.split(' ')
counter = {}

for word in longstring2:
    print(word)
    print(longstring2)
    print(counter)
    if word not in counter:
        counter[word] = 0  # w tym miejscu tworzymy według klucza word nową wartość = 0 ponieważ linię niżej zwiększamy ją do 1
                            # jest to zabezpieczenie aby nie powielać if'ów i nie kombinować z iteracjami
    counter[word] += 1      # tu dodajemy właścią iterację wartości o ile word w słowniku jest nową wartością
    print(word)
print(counter)

text = 'asd edf sd a s d edfrd'
text1 = text.replace(' ', '')
text1 = (' '.join(text1))
print(text1)



