"""
Given an integer, , print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n.
Each value should be space-padded to match the width of the binary value of n.
n = 7
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
"""

def print_formatted(number):
    # your code goes here
    n = len(str(bin(number))[2:])
    for i in range(1, number+1):
        print("{:>{}s} {:>{}s} {:>{}s} {:>{}s}".
        format(str(i),n,str(oct(i))[2:],n,str(hex(i))[2:].upper(),n,str(bin(i))[2:],n))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

