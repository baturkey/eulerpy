"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

def is_leap_year(y):
    if y % 4 > 0:
        return False
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    return True

def num_days(m, y):
    if m == 1:
        return 31
    if m == 2:
        if is_leap_year(y):
            return 29
        else:
            return 28
    if m == 3:
        return 31
    if m == 4:
        return 30
    if m == 5:
        return 31
    if m == 6:
        return 30
    if m == 7:
        return 31
    if m == 8:
        return 31
    if m == 9:
        return 30
    if m == 10:
        return 31
    if m == 11:
        return 30
    if m == 12:
        return 31

start = 1
count = 0
for y in xrange(1900, 2001):
    for m in xrange(1, 13):
        #print m, y
        if(start % 7 == 0 and 1901 <= y <= 2000):
            count += 1
        start += num_days(m, y)
print count
