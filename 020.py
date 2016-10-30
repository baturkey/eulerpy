"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""


from math import factorial

digits = list(str(factorial(100)))
sum = 0
for digit in digits:
    sum += int(digit)
print sum

            
