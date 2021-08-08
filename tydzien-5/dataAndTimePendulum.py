# http://
# biblioteka do pracy z datą i czasem
import pendulum

dt = pendulum.now()
print(dt.format('dddd DD MMMM YYYY', locale='pl'))
print(dt.format('DDMMYYYY', locale='pl'))

dt1 = pendulum.date(2021, 7, 1)
print(dt1)

