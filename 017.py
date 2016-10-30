"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

small_numbers = {0: "",
                 1:  "one",
                 2:  "two",
                 3:  "three",
                 4:  "four",
                 5:  "five",
                 6:  "six",
                 7:  "seven",
                 8:  "eight",
                 9:  "nine",
                 10: "ten",
                 11: "eleven",
                 12: "twelve",
                 13: "thirteen",
                 14: "fourteen",
                 15: "fifteen",
                 16: "sixteen",
                 17: "seventeen",
                 18: "eighteen",
                 19: "nineteen"}

tens = {2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"}

def stringify(n):
    global small_numbers
    if n == 1000:
        return "one thousand"
    if n % 100 == 0:
        return small_numbers[n / 100] + " hundred"
    if n > 99:
        q = n // 100
        return small_numbers[q] + " hundred and " + stringify(n % 100)
    elif n < 20:
        return small_numbers[n]
    else:
        q = n // 10
        return tens[q] + "-" + small_numbers[n % 10]
        
sum = 0
for n in xrange(1, 1001):
#    print stringify(n)
    sum += len(stringify(n).replace(" ", "").replace("-", ""))
print sum




