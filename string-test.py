'''
string jest niemutowaly nie możey go podmieniać możemy przeprowadzić operacje i zapisać nowy string


'''

text = '  ..  world hello   .'
text2 = 'cos tam innego'
test = "asd, gthy, miojeiowe, wwwwxxx"
text1 = str(text.split(' '))
print(text1)
print(type(text1))
print(type(text))
print(type(text2))
print(type(test))
print(len(text))
print('llo' in text)
print(text.find('ll'))
print(' '.join(text2))
print(text2)
print('*' *50)
print(text)
print(len(text))

test1 = text.strip(" .") # strip usuwa domyślnie strip() białe znaki przed i za napisem lub znaki zdefiniowane strip(" .") spacje i kropiki
print('*' *50)
print(test1)
print(len(test1))
test1 = text.strip().split(' ')
print('*' *50)
print(test1)
print(len(test1))
print('*' *50)
test2 = test
print(test2)
a = 10000000
b = 100000010
c = a + b
print(f'{c:,}')
str1 = "We are working on {0} with {1}".format("Advanced Python", "Kornel")
from string import Template
templ = Template("przerabiamy teraz ${title} z ${author}")
str3 = templ.substitute(title="Advanced Python", author="kornel")
print(str3)
data = {
    "author": "kornel",
    "title": "Advanced Python"
}
str4 = templ.substitute(data)
print(str4)
