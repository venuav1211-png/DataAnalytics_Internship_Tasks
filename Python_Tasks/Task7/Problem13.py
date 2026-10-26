# Problem Name: Sherlock and the Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    freq = Counter(s)
    counts = Counter(freq.values())
    
    if len(counts) == 1:
        return "YES"
    if len(counts) > 2:
        return "NO"
    
    c1, count1 = list(counts.keys())[0], list(counts.values())[0]
    c2, count2 = list(counts.keys())[1], list(counts.values())[1]
    
    if (c1 == 1 and count1 == 1) or (c2 == 1 and count2 == 1):
        return "YES"
    if (abs(c1 - c2) == 1) and (count1 == 1 or count2 == 1):
        if (c1 > c2 and count1 == 1) or (c2 > c1 and count2 == 1):
            return "YES"
            
    return "NO"

if __name__ == '__main__':
    s = input()
    result = isValid(s)
    print(result)