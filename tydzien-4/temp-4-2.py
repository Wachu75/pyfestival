a1 = 0
a2 = []


def fibonaci_recursion(value):
    if value == 0:
        a1 = 0
        return a1
    if value == 1:
        a2 = [0, 1]
        return a2


    return fibonaci_recursion(value-1)

# 3