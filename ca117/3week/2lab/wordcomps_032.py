#!/usr/bin/env python3

import sys

def endsiary(words):
    '''Checking if a word ends with iary'''
    counter = 0
    for w in words:
        if w[-4:] == "iary":
            counter += 1
    return counter

words = [w.strip() for w in sys.stdin]
vowels = {'a', 'e', 'i', 'o', 'u'}

highest = 0
for word in words:
    if word.count("e") > highest:
        highest = word.count("e")

#words with all vowels
wav = sorted([word for word in words if vowels.issubset(word)], key=len)[0]

print("Shortest word containing all vowels:", wav)
print("Words ending in iary:", endsiary(words))
print("Words with most e's:", [w for w in words if w.count("e") == highest])
