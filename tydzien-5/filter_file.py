# import os

even = []
with open('sample.txt') as input_file:
    for line in input_file:
        result = int(line.strip())

        if result % 2 == 0:
            even.append(result)

print(even)

# if os.stat('even1.txt').st_size == 0:
#    print('nie ma nic')
# else:
#    print('plik istnieje')


with open('even.txt', 'w') as output_file:
    for number in even:
        output_file.write(f'{number}\n')

