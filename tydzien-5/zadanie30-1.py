from calendar import isleap
from datetime import date, datetime, timedelta

# important notice!
# to checking how calculate program next_birthday date in leap year and next after leap year ?

def when_birthday(birthday):
    if today == birthday:
        print("Wszystkiego Najlepszego z okazji Twoich urodzin")

    elif today > birthday:
        scope = birthday - today
        print(f'Urodziny były {abs(scope.days)} dni temu')
        scope1 = 365 - abs(scope.days)
        next_birthday = date.today() + timedelta(days=scope1)
        scope = next_birthday - today
        print(f'Do następnych urodzin pozostało {scope.days} dni: ')
        print('Będzie to: ', next_birthday.strftime("%d.%m.%y"))
        print('a dzień Twoich urodziń przypadnie: ', birthday.strftime("%A"))
    else:
        scope = abs(today - birthday)
        print('Do urodzin pozostało dni: ', scope.days)
        print('Będzie to: ', birthday.strftime("%A"))


def add_years(d, years):
    new_year = d.year + years
    try:
        return d.replace(year=new_year)
    except ValueError:
        if d.month == 2 and d.day == 29 and isleap(d.year) and not isleap(new_year):
            return d.replace(year=new_year, day=28)
        raise


today = date.today()
print('Dzisiaj jest: ', today) #.strftime("%A.%B.%Y"))
print('*' * 50)
birthday_month = int(input('podaj miesiąc urodzin: '))
birthday_day = int(input('podaj dzień urodzin: '))
birthday = date(today.year, birthday_month, birthday_day)

when_birthday(birthday)
