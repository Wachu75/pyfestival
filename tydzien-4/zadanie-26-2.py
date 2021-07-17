# proszę nie komentować tego co filtruję
# mam czasami po prostu takie coś, cytuję za Mirosławem Zelent i jego filmami "a co by było gdyby ....?"

name = ['ala nowak', 'monika dZIeciołp', 'jacek kulAwyr', 'wieslaw zmrozony', 'krzysztof ogrodnik', 'alA wroNa']

names2 = name[0].split(' ')  #.split(' ') rozbija string po spacjach i zwraca liste
names2 = names2[1].title()
names3 = [name[n].title() for n, names in enumerate(name)]
names4 = sorted(names3, key=lambda x: x[-1]) # po ostatniej literze imię nazwisk(o)
#names5 = [name[n].title().split(' ') for n, names in enumerate(name)]
names5 = sorted(names3, key=lambda x: x[0])  # po pierwszej literze (i)mię nazwisko

# nie działa prawidłowo na polskich literach jak było ostatnie ł w
# nazwisku to wywaliło na koniec listy !? czy ja czgoś tu nie rozumiem - do sprawdzenia!

print(names3)
print(names4)
print(names5)
print('-' * 50)

name_test = ['a a', 'b f', 'n ł', 'x ą', 'q w', 'a z', 'c v', 'x ź', 'ó ń', 'ą ę']
names_test = [name_test[n].title() for n, names in enumerate(name_test)]
names_test = sorted(names_test, key=lambda x: x[0])
names_test1 = sorted(names_test, key=lambda x: x[-1])
print(names_test) # sortuje po pierwszej literze i w efekcie mam na końcu listy ą ź ń ę
print(names_test1) # sortuję po ostatniej literze i w efekcie mam na końcu listy .....



