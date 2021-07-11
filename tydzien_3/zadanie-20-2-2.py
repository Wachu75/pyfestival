def count_numbers(numbers: list, count_odd: bool = True, coun_even: bool = True):
    odds = [odd for odd in numbers if odd % 2 != 0]
    even = [evv for evv in numbers if evv % 2 == 0]

    total = 0 if not count_odd else len(odds)
    total += 0 if not coun_even else len(even)

    return  total

print(count_numbers([1,2,3,4,5,6,7,8,9]))
print(count_numbers([1,2,3,4,5,6,7,8,9], count_odd=False))
print(count_numbers([1,2,3,4,5,6,7,8,9], coun_even=False))

