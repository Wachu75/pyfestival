from math import floor

primes = []

n = 3
while len(primes) < 10:
    is_prime = True
    for div in range(2,floor(n**0.5)+1):
        if n % div == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(n)

    n += 1
print(primes)