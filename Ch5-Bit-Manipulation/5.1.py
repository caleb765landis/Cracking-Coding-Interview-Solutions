"""
5.1 Insertion: 
You are given two 32-bit numbers, N and M, and two bit positions, i and
j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
can assume that the bits j though i have enough space to fit all of M. That is, if 
M=10011, you can assume that there are at least 5 bits between j and i. You would not, for example,
have j=3 and i=2, because M could not fully fit between bit 3 and bit 2.

EXAMPLE
Input: N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100

Hints: #137, #169, #215
Q: pg.115
A: pg.276
"""

from BitTasks import *

def main():
    # m = 10011
    m = 19
    # n = 10000000000
    n = 1024

    # a = 10001001100
    a = insertMintoN(m, n, 2, 6)
    print(bin(a))

    # m = 10
    m = 2
    # n = 11111111111
    n = 2047

    # a = 11000101111
    a = insertMintoN(m, n, 4, 8)
    print(bin(a))


def insertMintoN(m, n, i, j):
    left_n = clearBitsIthrough0(n, j)
    right_n = clearMSBitthroughI(n, i)

    cleared_n = left_n | right_n

    shifted_m = m << i
    return cleared_n | shifted_m

if __name__ == '__main__':
    main()