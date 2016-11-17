"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""


f = open("resources/names.txt", "r")
lines = sorted(map(lambda x: x.replace("\"", ""), f.readline().split(",")))
f.close()

total = 0
for x in xrange(0, len(lines)):
    total += (x+1) * reduce(lambda x, y: x + y, map(lambda x: ord(x) - 64, list(lines[x])))

print total
