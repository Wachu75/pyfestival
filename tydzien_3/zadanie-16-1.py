salary_base = 2000
year = int(input('podaj staż pracy w latach'))
hours = int(input('podaj ilość przepracowanych godzin'))
sales_pices = int(input(' ilosć sprzedanych sztuk'))
bonus_sales = 0
bonus_activity = 0
salary = 0
salary = (salary_base + (salary_base * 0.02))
bonus_activity = salary_base * 0.02
salary = (salary_base + (salary_base * 0.1)) if year > 2 else salary
bonus_sales = salary_base * 0.25 if sales_pices > 30 else bonus_sales
bonus_activity = salary_base * 0.08 if hours > 160 and year > 1 else bonus_activity

print(salary)
print(bonus_sales)
print(bonus_activity)

