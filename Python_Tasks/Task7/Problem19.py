# Problem Name: Weighted Uniform Strings
# HackerRank Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import math
import os
import random
import re
import sys

def weightedUniformStrings(s, queries):
    weights = set()
    current_weight = 0
    prev_char = ''
    
    for char in s:
        if char == prev_char:
            current_weight += (ord(char) - ord('a') + 1)
        else:
            current_weight = (ord(char) - ord('a') + 1)
            prev_char = char
        weights.add(current_weight)
        
    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == '__main__':
    s = input()
    queries_count = int(input().strip())
    queries = [int(input().strip()) for _ in range(queries_count)]
    result = weightedUniformStrings(s, queries)
    print('\n'.join(result))