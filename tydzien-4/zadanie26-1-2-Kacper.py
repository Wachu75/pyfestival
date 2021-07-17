def map_and_filter(numbers: list) -> list:
    return list(
        filter(
            lambda x: x % 2 == 0,
            map(lambda x: x ** 0.5, numbers)
        )
    )

numbers = [1,2,3,4,5,6,7,8,9,10,16,25,36,49]

def test_map_and_filter():
    a = [16,36,25,49]
    assert map_and_filter(a) == [4,6]



def capitalize(word):
    return word[0].upper() + word[1:].lower()

def clean_up_names(persons: list) -> list:
    persons = map(lambda person: person.lower(), persons)
    persons = map(lambda person: person.split(' '), persons)
    persons = map(lambda person: capitalize(person[0]) + ' ' + capitalize(person[1]), persons)
    persons = sorted(persons, key=lambda person: person.split(' ')[1])
    return list(persons)

def test_clean_up_names():
    #given
    persons = [
        'jAn KowalsKi',
        'mariA Nowak',
        'Zenon Brat'
    ]
    #when
    cleaned = clean_up_names(persons)

    #then
    assert cleaned == [
        'Zenon Brat',
        'Jan Kowalski',
        'Maria Nowak'
    ]