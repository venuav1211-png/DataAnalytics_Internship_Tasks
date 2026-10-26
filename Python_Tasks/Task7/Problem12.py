# Problem Name: Making Anagrams
# HackerRank Link: https://www.hackerrank.com/challenges/making-anagrams/problem

import math
import os
import random
import re
import sys
from collections import Counter

def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    diff = c1 - c2
    diff2 = c2 - c1
    return sum((diff + diff2).values())

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)
    print(result)