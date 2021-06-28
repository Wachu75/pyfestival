import datetime
from datetime import date

today = date.today()
day = date(today.year, 2, 10)
impreza = day.strftime("%d.%m.%y")
formatted = today.strftime("%A.%B.%Y")
print(formatted)
print(day)
#print(f'dziś jest {today}')

#print(int(date.today().year + 1))
print(' ')
if day > today:
    diff = day - today #(today.year + 1)
    next_year = int(today.year) + 1
    print(next_year)
    print(diff.days)

else:
    diff = today - day
    next_year = today.year + 1
    today1 = today.year
    print(datetime.timedelta(1))
    #print(max(next_year-today1))
    #print(diff)

start_date = datetime.datetime(2006, 7, 3)
end_date = datetime.datetime(2012, 12, 21)
years = range(start_date.year, end_date.year + 1)
start, end = start_date, end_date + datetime.timedelta(1)
for year in years:
    year_start = datetime.datetime(year, 1, 1, 0, 0)
    year_end = datetime.datetime(year + 1, 1, 1, 0, 0)
    print(year, min(end, year_end) - max(start, year_start))

day = date.today()
day += datetime.timedelta(days=1)
print(day)

event = datetime.datetime.now()
print(event.hour)
print(event.minute)
print(event.strftime('%H:%M'))