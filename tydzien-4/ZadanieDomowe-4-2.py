def fibonacci(value):
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


def fibonacci_recursion(value):
    if value == 0:
        return 0
    if value == 1:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


for n in range(11):
    print(fibonacci(n))

print('*' * 50)
# print(fibonacci_recursion(5))  # błędy nie działa prawidłowo



#
# def test_fibonacci():
#     assert fibonacci(0) == [0]
#     assert fibonacci(1) == [0, 1]
#     assert fibonacci(2) == [0, 1, 1]
#     assert fibonacci(3) == [0, 1, 1, 2]
#     assert fibonacci(5) == [0, 1, 1, 2, 3, 5]
#     assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]