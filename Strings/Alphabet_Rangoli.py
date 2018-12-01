"""
You are given an integer, . Your task is to print an alphabet rangoli of size .
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""

def print_rangoli(size):
    # your code goes here
    #print(chr(97))
    for i in range(-1*size+1,size,1):
        #print(chr(97+abs(i)))
        strs = ""
        if size-abs(i) == 1:
            strs = chr(97+abs(i))
        else:
            for j in range(-1*(size-abs(i))+1, size-abs(i),1):
                strs += chr(97+abs(i)+abs(j))
        print("{:-^{}s}".format('-'.join(list(strs)),4*n-3))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)