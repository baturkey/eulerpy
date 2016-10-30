import string
"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(x):
    s = str(x)
    r = ''.join(list(reversed(list(s))))
    return s == r

max = 0
for i in range(99, 1000):
    for j in range(99, 1000):
        product = i * j
        if(product > max and is_palindrome(product)):
            max = product;
print max
        
