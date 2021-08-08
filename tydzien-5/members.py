
from json import load, dump

with open('data.json') as data:
    course = load(data)
    print(course)
    print(f'nazwa kursu {course["name"]}')
    print('zapisani kursanci: ')
    for member in course['members']: # iteruję po polach ukrytych dla members czyli w tym przypadku po liście słowników
        print(f' - {member["first_name"]} {member["last_name"]}')

    firs_name = input('imie:')
    last_name = input('nazwisko:')

# bez wciecia with poniżej też działa ale sprawia to że mamy na 100% dostęp do member

    with open('data.json', 'w') as data:      #z json jest tak że chcemy podmienić całą zawartość pliku.json na nową czyli używamy 'w'
        course['members'].append({
            'id': len(course['members']) + 1,
            'first_name': firs_name,
            'last_name': last_name
        })
        dump(course, data)  # course to jest nasz objekt i co chcemy zapisać czyli nasz pointer data
