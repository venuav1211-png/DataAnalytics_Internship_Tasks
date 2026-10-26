# Problem Name: Game of Thrones - I
# HackerRank Link: https://www.hackerrank.com/challenges/game-of-thrones/problem

import math
import os
import random
import re
import sys
from collections import Counter

def gameOfThrones(s):
    counts = Counter(s)
    odd_count = sum(1 for count in counts.values() if count % 2 != 0)
    
    if len(s) % 2 == 0:
        return "YES" if odd_count == 0 else "NO"
    else:
        return "YES" if odd_count == 1 else "NO"

if __name__ == '__main__':
    s = input()
    result = gameOfThrones(s)
    print(result)