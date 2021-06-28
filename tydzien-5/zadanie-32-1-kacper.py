from csv import reader, writer

result = []

with open('transakcje-1.csv', encoding='utf8') as input_file:
    content = reader(input_file, delimiter=',')
    next(content) #pomijamy pierwsza linie
    for line in content:
        created_at, description, value = line
        print(int(value))
        if int(value) > 0:
            result.append(line)

print(result)

with open('income.csv', 'w', encoding='utf8', newline='') as output_file:
    content = writer(output_file, delimiter=',')
    for line in result:
        print(line)
        content.writerow(line)



