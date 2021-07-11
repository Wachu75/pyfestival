def find_divisors(a):
    # divisors = set()
    # for divisor in range(2, a+1):
    #     if a % divisor == 0:
    #         divisors.add(divisor)
    # return divisors
    return {divisor for divisor in range(2, a+1) if a % divisor == 0}


def calculate_common_divisor(a, b, offset):
    common_divisors = find_divisors(a) & find_divisors(b)
    common_divisors = [divisor for divisor in common_divisors if divisor >= offset]
    return sorted(list(common_divisors)) if len(common_divisors) > 0 else None

test1 = calculate_common_divisor(3, 6)
print(test1)

