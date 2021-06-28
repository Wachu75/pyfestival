# palindrom anagram
word1 = input('podaj pierwsze slowo')

word2 = input('podaj drugie slowo')

word1 = ''.join(word1.split(' '))

word2 = ''.join(word2.split(' '))

if word1 == word2[::-1]:
    print('to sa palindromy')
else:
    print('to nie są palindromy')

