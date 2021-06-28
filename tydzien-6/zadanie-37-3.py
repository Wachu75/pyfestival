'''
napisz program któy będzie przechowywał wszystkie twoje spotaknia
Informacje o spotkaniach przechowuj w pliku meetings.json

kazde spotkanie trwa godzine
spotkania moga miec różne tytuły
na dany dzien, na daną godzinę może być zapisane tylko jedno spotkanie
Kalendarz posiada następujące metody:
    wyświetlanie wszystkich spotkań(posortowanych po dacie
    sprawdzenie czy dany termin ( data i godzina) jest wolna
    znalezienie najbliższej wolnej godziny w określonej dacie następnej dacie

meetings.json
    {'tytul': tytul,

'''
from datetime import datetime, timedelta
from json import load, dump

class OpenFile:
    pass

class WriteFile:
    pass


class Meeting:
    def __init__(self, m_date, title):
        self.m_date = m_date
        self.title = title


class Calendar:
    def __init__(self):
        self.meetings = {}

    def check_if_available(self, date: datetime):
        return date not in self.meetings

    def add_meeting(self, meeting: Meeting):
        if self.check_if_available(meeting.m_date):
            self.meetings[meeting.m_date] = meeting

    def next_available_slot(self, date: datetime):
        meetind_date = date
        while not self.check_if_available(meetind_date):
            meetind_date += timedelta(minutes=60)
        return meetind_date


calendar = Calendar()
with open('meetings.json') as file:
    data = load(file)
    for item in data:
        meeting = Meeting(datetime.strptime(item['date'], '%d.%m.%Y %H:%M'), item['title'])

        calendar.add_meeting(meeting)

if __name__ == '__main__':
    while True:
        option = input('[l] lista [d] dodaj:')

        if option == 'l':
            for _, meeting in calendar.meetings.items():
                print(f'{meeting.m_date}: {meeting.title}')

        elif option == 'd':
            title = input('tytuł spotkania: ')
            date = input('data: ')
            meeting_date = datetime.strptime(date, '%d.%m.%Y %H:%M')
            calendar.add_meeting(Meeting(meeting_date, title))

            with open('meetings.json', 'w') as file:
                data = []
                for meeting in calendar.meetings.values():
                    data.append({
                        'title': meeting.title,
                        'date': meeting.m_date.strftime('%d.%m.%Y %H:%M')
                    })
                dump(data, file)

        elif option == 'q':
            break

        else:
            print('o co ci chodzi?')