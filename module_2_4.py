numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

not_primes_promo = set()
primes = []

for i in numbers:
    for k in range(2, i + 1):
        if i % k == 0 and i != k:
            not_primes_promo.add(i)

    if i not in not_primes_promo and i != 1:
        primes.append(i)

print('Primes:', primes)

not_primes = (list(not_primes_promo))
print('Not Primes:', not_primes)
