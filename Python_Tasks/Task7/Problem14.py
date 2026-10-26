# Problem Name: Anagram
# HackerRank Link: https://www.hackerrank.com/challenges/anagram/problem

import math
import os
import random
import re
import sys
from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    changes = 0
    for char in c1:
        if c1[char] > c2[char]:
            changes += c1[char] - c2[char]
    return changes

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input()
        result = anagram(s)
        print(result)