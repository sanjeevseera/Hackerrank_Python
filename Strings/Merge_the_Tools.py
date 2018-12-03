"""
Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in .
Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once.
In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .
Sample Input:
AABCAAADA
3
Sample Output:
AB
CA
AD
"""

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        s = string[i:i+k]
        n = 0
        while n < len(s):
            while n < len(s) and s.index(s[n]) < n:
                if n+1 < len(s):
                    s = s[:n] + s[n+1:]
                else:
                    s = s[:n]
            else:
                n+=1
        print(s)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

