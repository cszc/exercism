def sieve(limit):
    primes = range(2, limit)
    for i in primes:
        primes = [x for x in primes if x % i != 0 or x == i]
    return primes
