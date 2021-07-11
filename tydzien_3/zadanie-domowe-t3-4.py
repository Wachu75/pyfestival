def filter_even(number: list) -> list:
    return [a for a in number if a % 2 == 0]


def filter_words(word: list) -> list:
    return [a for a in word if len(a) > 4 and len(a) < 8]  # 4 < len(a) < 8


def find_divisors(a):
    return {d for d in range(2, a + 1) if a % d == 0}
    # nawiasy {} są w celu zapewnienia zwracanej wartości jako - zbiór / set


def filter_greatest_divisor(a, b):
    div_a = find_divisors(a)
    div_b = find_divisors(b)
    return max(div_a & div_b)


print(type(find_divisors(1)))

print(filter_greatest_divisor(2, 8))
print(filter_greatest_divisor(120, 60))
print(filter_greatest_divisor(25, 30))


def get_fibonaci(limit):
    if limit == 0:
        return []
    if limit == 1:
        return [0]
    a = 0
    b = 1
    result = [a, b]
    while len(result) < limit:
        a, b = b, a + b
        result.append(b)
        # 0,1,1,2,3,5,8,13....

    return result


print(get_fibonaci(20))
