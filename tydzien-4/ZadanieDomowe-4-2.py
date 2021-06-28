def fibonaci_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 0

    return fibonaci_sum(n - 1) + fibonaci_sum(n - 2) + 1


def test_fibonaci_sum():
    assert fibonaci_sum(0) == 0
    assert fibonaci_sum(1) == 0
    assert fibonaci_sum(2) == 1
    assert fibonaci_sum(3) == 2
    assert fibonaci_sum(5) == 0 + 1 + 1 + 2 + 3

print(fibonaci_sum(5))
