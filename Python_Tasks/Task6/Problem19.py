# Problem Name: Company Logo
# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem[cite: 14]

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    counted = Counter(sorted(s))
    for char, count in counted.most_common(3):
        print(f"{char} {count}")