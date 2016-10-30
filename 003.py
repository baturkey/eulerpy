from math import sqrt

"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def is_prime(x):
    for n in range(x // 2, 2, -1):
        if(x % n == 0):
            break;
    else:
        return True
    return False

x = 600851475143
for n in range(int(sqrt(x)), 2, -1):
    if(x % n == 0 and is_prime(n)):
        print n
        break
