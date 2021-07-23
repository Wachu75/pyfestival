def fibonaci_sum(value):
    fibonaci = []
    if value == 0:
        fibonaci.append(0)
        return fibonaci
    if value == 1:
        fibonaci = [0, 1]
        return fibonaci
    fibonaci = [0, 1]
    start = 1
    temp_value = 2
    for n in range(start, value):
        if len(fibonaci) <= temp_value:
            temp_value += 1
            fibonaci.append(fibonaci[n] + fibonaci[n-1])
    return fibonaci


# def fibonaci_recursion(value):
#
#     if value == 0:
#         fibonaci = 0
#         return fibonaci
#     if value == 1:
#         fibonaci = 1
#         return fibonaci
#     fibonaci = 2
#     fibonaci += fibonaci[value-1] + fibonaci[value]
#     return fibonaci_recursion(value-1)


for n in range(11):
    print(fibonaci_sum(n))




#
# def test_fibonaci_sum():
#     assert fibonaci_sum(0) == [0]
#     assert fibonaci_sum(1) == [0, 1]
#     assert fibonaci_sum(2) == [0, 1, 1]
#     assert fibonaci_sum(3) == [0, 1, 1, 2]
#     assert fibonaci_sum(5) == [0, 1, 1, 2, 3, 5]
#     assert fibonaci_sum(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]