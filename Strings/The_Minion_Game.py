"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

"""
import re

def minion_game(string):
    # your code goes here
    d = {'Stuart':0, 'Kevin':0}
    for match in re.finditer("[A|E|I|O|U]",string) :
        d['Kevin'] += len(s)-match.start()
    d['Stuart'] += (len(string)*(len(string)+1)//2) - d['Kevin']
    if d['Stuart'] > d['Kevin']:
        print("Stuart", d['Stuart'])
    elif d['Stuart'] == d['Kevin']:
        print("Draw")
    else:
        print("Kevin", d['Kevin'])


if __name__ == '__main__':
    s = input()
    minion_game(s)