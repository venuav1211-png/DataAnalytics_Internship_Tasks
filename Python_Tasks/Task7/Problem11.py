# Problem Name: Two Strings
# HackerRank Link: https://www.hackerrank.com/challenges/two-strings/problem

import math
import os
import random
import re
import sys

def twoStrings(s1, s2):
    if set(s1) & set(s2):
        return "YES"
    return "NO"

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        print(result)