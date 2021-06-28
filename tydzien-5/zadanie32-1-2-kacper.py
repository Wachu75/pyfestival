sumary = 0
with open('income.csv') as handler:
    for line in handler:
        line_arr = line.strip().split(',')
        created_at, title, value = line_arr
        sumary += int(value)

print(sumary)
