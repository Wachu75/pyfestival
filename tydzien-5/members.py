
from json import load, dump

with open('data.json') as data:
    course = load(data)
    print(course)
    print(f'nazwa kursu {course["name"]}')
    print('zapisani kursanci: ')
    for member in course['members']: # iteruję po polach ukrytych dla members czyli w tym przypadku po liście
        print(f' - {member["first_name"]} {member["last_name"]}')

    firs_name = input('imie:')
    last_name = input('nazwisko:')

# bez wciecia with poniżej też działa

    with open('data.json', 'w') as data:
        course['members'].append({
            'id': len(course['members']) + 1,
            'first_name': firs_name,
            'last_name': last_name
        })
        dump(course, data)
