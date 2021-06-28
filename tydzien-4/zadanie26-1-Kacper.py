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