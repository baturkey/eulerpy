from math import sqrt
"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
factor_dict = {}

def is_prime(x):
    for n in range(int(sqrt(x)), 2, -1):
        if(x % n == 0):
            break;
    else:
        return True
    return False

def prime_factors(x):
    output = []
    for n in range(2, x+1):
        if x % n == 0 and is_prime(n):
            output.append(n)
            output.extend(prime_factors(x / n))
            break
    return output

for factors in [prime_factors(x) for x in range(2, 21)]:
    factor_set = set(factors)
    for prime in factor_set:
        prime_count = factors.count(prime)
        if not factor_dict.has_key(prime) or prime_count > factor_dict[prime]:
            factor_dict[prime] = prime_count

product = 1
for prime, count in factor_dict.iteritems():
    product *= prime ** count
print product
