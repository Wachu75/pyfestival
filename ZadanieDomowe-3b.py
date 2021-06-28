text= input('tekst do zaszyf')
option = input('1-odszyfrujj 2- zasz')

if option == '1':
    result = ''
    for char in text:
        if ord(char) >= ord('x'):
            result += chr(ord(char) - 23)
        else:
            result += chr(ord(char) + 3)
    print(result)
elif option == '2':
    result = ''
    for char in text:
        if ord(char) >= ord('d') or char == '#':
            result += chr(ord(char) - 3)
        else:
            result += chr(ord(char) + 23)
    print(result)
else:
    print('nie rozumiem')
