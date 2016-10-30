"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
from math import sqrt

def is_prime(x):
    for n in range(int(sqrt(x)), 2, -1):
        if(x % n == 0):
            break;
    else:
        return True
    return False

def primes():
    yield 2
    prime = 3
    counter = 1
    while counter < 10001:
        yield prime
        counter += 1
        prime += 2
        while(not is_prime(prime)):
            prime += 2

for prime in [x for x in primes()]:
    pass
print prime
