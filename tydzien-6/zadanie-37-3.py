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
        return date not in self.meetings            # zwróć datę jeżeli nie ma jej już w meetings czyli jeżeli jest dostępna

    def add_meeting(self, meeting: Meeting):        # odbieram obiekt klasy Meeting
        if self.check_if_available(meeting.m_date): # do metody check_if_available przekazuję datę z obiektu meeting
            # jeżeli jest True wykona się linia niżej:
            # do tego momentu rozumiem co się dzieje
            self.meetings[meeting.title] = meeting # dodane po komentarzu z ostatich lini poniżej - to działa
            #self.meetings[meeting.m_date] = meeting # do słownika meetings pod klucz "date" m_date obiektu meeting
            # (to jest nasz klucz) zapisz wartości obiektu klasy meeting  czyli oba pola ?
            # kiedy następuje przypisanie ??? czy przypisywane są oba pola na raz ???
            # jak rozumieć self.meetings[meeting.m_date] czy wartość meeting.m_date jest już zapisana w słowniku ?
            # jeżeli tak to kiedy to nastąpiło, jeżeli nie to jak to odczytać -> pod klucz date z słownika meetings
            # wpisz m_date a pod values title wartość title ?
            # skąd to wiadomo.
            # self.meetings[data_dziś] przecież jej jeszcze nie ma w słowniku
            # to chyba jest tak że jeżeli jej jeszcze nie ma to przypisz jak było w zadaniu 37-2 z report[apple.color] = 0
            # ja chyba nie rozumiem tego zapisu ponieważ cały czas próbuję to zapisać
            # self.meetings[meeting] = meeting czyli utwóz nową pozycję w słowniku i przypisz odpowiednio czały meeting
            # właśnie wprowadziłem zamiane w kodzie !!!!! albo jeszcze inaczej to równie dobrze mogło by być
            # if ...
            # self.meetings[meeting.title] = meeting ?
    # tego nie rozumiem co się tu wydażyło krok po kroku proszę o wyjaśnienie !!!
    '''
    6.10 rano niedziela jakby ktoś pytał czy jest wszystko ok.
    taki kod do wyjaśnienia co się dzieje 
    meeting1 = ('a', 1)
    meetings = {} tworze pusty słownik 
    meetings[0] = meeting1 #w słowniku pod indexem[0] gdzie 0 jest kluczem wprowadzam zmienną-dane
    meetings["2020-01-01"] = meeting1 #w słowniku pod jeszcze nie istniejącym kluczem "2020-01-01" tworzę-wprowadzam dane ('a',1)
    print(meetings) -> {0: ('a', 1), '2020-01-01': ('a', 1)}
    '''

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
            date = input('data w formacie dd.mm.yyyy hh:mm')
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