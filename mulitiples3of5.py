def solution(number):
    numbers = []
    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            numbers.append(num)
    return sum(numbers)

value = int(input('podaj liczbę: '))

print(solution(value))

