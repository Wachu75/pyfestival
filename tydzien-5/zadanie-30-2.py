# poproś użytkownika o datę rozpoczęcia , datę zakończenia , a także o jego dniówkę. w odpowiedzi powinna wyświetlić
# się informacja ile użytkownik zarobił
# spróbuj wyświetlić za pomocą pętli wszystkie dni pomiędzy dwiema datami z wyżej podanych
# policz podwójnie wynagrodzenie pracownika za pracę w soboty i niedziele


from datetime import date, datetime, timedelta

today = date.today()

print('Program liczy ilość przepracowanych dni z podanego zakresu w danym roku!!!')
day_start = int(input('podaj dzień rozpoczęcia pracy: '))
month_start = int(input('podaj miesiąc rozpoczęcia pracy: '))
start_date = date(today.year, month_start, day_start)
day_end = int(input('podaj dzień zakończenia pracy: '))
month_end = int(input('podaj miesiąc zakończenia pracy: '))
end_date = date(today.year, month_end, day_end)
salary = int(input('podaj wynagrodzenie za dzień pracy: '))

day = end_date - start_date
day1 = abs(day.days)+1
print(day1)
sunday_count = 0
saturady_count = 0

for d in range(int(day1)):
    week_day = date(today.year, month_start, day_start)
    week_day = week_day + timedelta(days=d)
    formatted = week_day.strftime("%A.%B.%Y")
    print(formatted)
    if week_day.strftime("%A") == "Sunday":
        sunday_count += 1
    if week_day.strftime("%A") == "Saturday":
        saturady_count += 1


print('niedziel w tym okresie czasu było: ', sunday_count)
print('sobót w tym okresie czasu było: ', saturady_count)

salary_normal_day = day1 - (sunday_count + saturady_count)
salary_extra_day = day1 - salary_normal_day
normal_salary = salary_normal_day * salary
extra_salary = (salary_extra_day*salary)*2
print(f'wynagrodzenie za normalne dni tygodnia = {normal_salary}')
print(f'wynagrodzenie za soboty i niedziele = {extra_salary}')
print(f'wynagrodzenie łącznie wynosi: {extra_salary+normal_salary}')



