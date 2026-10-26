# Problem Name: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

import math
import os
import random
import re
import sys

def separateNumbers(s):
    if len(s) < 2 or s.startswith('0'):
        print("NO")
        return
        
    for i in range(1, len(s) // 2 + 1):
        first_str = s[:i]
        first_num = int(first_str)
        current_str = first_str
        
        while len(current_str) < len(s):
            first_num += 1
            current_str += str(first_num)
            
        if current_str == s:
            print(f"YES {first_str}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input()
        separateNumbers(s)