def koszt(czas, ilosc, price: float=0.617) -> float:
    return czas * ilosc * price

czas = 1 #int(input('czas pracy'))

ilosc = 1 #int(input('ile godzin'))

print(koszt(czas, ilosc))

def count_numbers(numbers: list, count_odd: bool = True, count_even: bool = True):
    odds = [number for number in numbers if number % 2 != 0]
    even = [number for number in numbers if number % 2 == 0]

    total = 0 if not count_odd else len(odds)
    total += 0 if not count_even else len(even)
 
    return total

print(count_numbers([1,2,3,4,5,6,7]))
print(count_numbers([1,2,3,4,5,6,7], count_odd=False))
print(count_numbers([1,2,3,4,5,6,7], count_even=False))