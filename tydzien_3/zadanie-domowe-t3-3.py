def count_vowels(text):
    return sum([char in 'aąeęiouy' for char in text])
    #return sum([1 if char in 'aąeęiouy' else 0 for char in text]) # Kacper
print(count_vowels('ala'))
# 2
print(count_vowels('programowanie'))
print(count_vowels('ile samogłosek jest w tym zdaniu'))
