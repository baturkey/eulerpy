"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt

prime_list = [3]

def is_prime(x):
    output = False
    root = sqrt(x)

    global prime_list
    for prime in prime_list:
        if prime > root:
            prime_list.append(x)
            output = True
            break

        if x % prime == 0:
            break

    return output

def primes(limit):
    yield 2
    prime = 3
    while prime < limit:
        yield prime
        prime += 2
        while(not is_prime(prime)):
            prime += 2

print sum([x for x in primes(2000000)])
