from datetime import datetime, timedelta
from datetime import date

today = date.today()
day = date(today.year, 7, 23)
impreza = day.strftime("%d.%m.%y")  # string format time day zostanie sformatowany do string'a
formatted = today.strftime("%A.%B.%Y")
print(formatted)
print(day)
#print(f'dziś jest {today}')

#print(int(date.today().year + 1))
print('-' * 50)
if day > today:
    diff = day - today #(today.year + 1)
    next_year = int(today.year) + 1
    #print(next_year)
    print(diff.days)

else:
    diff = today - day
    next_year = today.year + 1
    today1 = today.year
    #print(datetime.timedelta(1))
    #print((next_year-today1))
    print(diff)

start_date = datetime(2006, 7, 3)
end_date = datetime(2012, 12, 21)
years = range(start_date.year, end_date.year + 1)
start, end = start_date, end_date + timedelta(1)
for year in years:
    year_start = datetime(year, 1, 1, 0, 0)
    year_end = datetime(year + 1, 1, 1, 0, 0)
    print(year, min(end, year_end) - max(start, year_start))

day = date.today()
day += timedelta(days=7)
#print(day)

event = datetime.now()
print(event.hour)
print(event.minute)
print(event.strftime('%H:%M'))

data1 = input('dd.mm.rrrr ')
d = datetime.strptime(data1, '%d.%m.%Y')
print(d)

