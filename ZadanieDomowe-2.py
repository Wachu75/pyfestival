from math import pow

print('podaj na ktory system chcesz dokonać zamiany')
key = input('na dziesiętny D, na dwójkowy Z: ')

def conv(value, key):
    pass
rest = 0
score = []
if key == 'z' or key == 'Z':
    value = int(input('podaj liczbę w systemie dziesiętnym: '))
    while value != 0:
        values = value % 2
        if values == 0:
            score.append('0')
        else:
            score.append('1')
        value = value // 2

    score.reverse()
    score = (''.join(score))
    print(score)
    ## wersja Kacpra print(f'wartość w systemie binarnym: {values:b}') :b oznacza wartość w systemie binarnym ;-)
score = 0
if key == 'd' or key == 'D':
    value = input('podaj liczbę w systemie dwójkowym: ') #10100 = 20
    #print(type(value))
    #value = (' '.join(value))
    #print(value)
    #value = reversed(value)
    value = value[::-1]
    #print(value)
    for number,values in enumerate(value):
        score += int(values) * int(pow(2,int(number)))
        #print(f'values: {values}')
        #print(f'number: {score}')

    ## wersja Kacpra:
    # for index,number in enumerate(value):
    # result += int(number) * 2 * (len(value)-index - 1)

print(int(score))



