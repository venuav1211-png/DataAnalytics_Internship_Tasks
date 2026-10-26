# Problem Name: Funny String
# HackerRank Link: https://www.hackerrank.com/challenges/funny-string/problem

import math
import os
import random
import re
import sys

def funnyString(s):
    r = s[::-1]
    s_diff = [abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s))]
    r_diff = [abs(ord(r[i]) - ord(r[i-1])) for i in range(1, len(r))]
    
    return "Funny" if s_diff == r_diff else "Not Funny"

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input()
        result = funnyString(s)
        print(result)