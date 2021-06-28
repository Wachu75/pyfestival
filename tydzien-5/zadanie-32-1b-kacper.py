from csv import reader, writer

result = []

with open('transakcje-1.csv', 'r', encoding='utf8') as input_file:
    next(input_file) #pomijamy pierwsza linie
    for line in input_file:
        line_as_list = line.strip().split(',')
        created_at, description, value = line_as_list
        print(int(value))
        if int(value) > 0:
            result.append(line)

print(result)

with open('income.csv', 'w', encoding='utf8') as output_file:
    output_file.writelines(result)

