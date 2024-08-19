#!/uar/bin/env python3

import sys

def anagrams(word, comp):
    anagram = {}

    for char in word:
        if char not in anagram:
            anagram[char] = 1
        else:
            anagram[char] += 1
    
    for char in comp:
        if char not in anagram:
            return False
        else:
            anagram[char] -= 1

    for char in anagram:
        if anagram[char] != 0:
            return False
    return True

for line in sys.stdin:
    w, c = line.strip().split()
    print(anagrams(w, c))
