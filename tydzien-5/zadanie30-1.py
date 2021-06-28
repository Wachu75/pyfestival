
from datetime import date

today = date.today()
birthday = date(today.year, 1, 9)

if today > birthday:
    birthday = date(today.year + 1, 1, 9)
    print(birthday-today)
    print(birthday.strftime("%A"))
else:
    diff = birthday - today
    print(diff.days)
    print(birthday.strftime("%A"))
