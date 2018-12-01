"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = tuple(map(int, input().split(" ")))
for i in range(-N//2+1, N//2+1, 1):
    j = N-(abs(i)*2)
    if abs(i) == 0:
        print("{:-^{}s}".format("WELCOME",M))
    else:
        print("{:-^{}s}".format(".|."*j,M))


