"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

seq_dict = {}

def do_seq(n, length):
    global seq_dict
    if n == 1:
        return length

    if seq_dict.has_key(n):
        return seq_dict[n] + length
    
    if n % 2 == 0:
        calc = n / 2
    else:
        calc = 3 * n + 1

    return do_seq(calc, length + 1)

def seq_length(n):
    global seq_dict
    if seq_dict.has_key(n):
        return seq_dict[n]

    output = do_seq(n, 1)
    
    seq_dict[n] = output
    return output

max = 0
num = 0
for x in xrange(1, 1000000):
    length = seq_length(x)
    if length > max:
        max = length
        num = x
print num

