# Problem Name: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem

import math
import os
import random
import re
import sys

def pangrams(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    s_set = set(s.lower())
    if alphabet.issubset(s_set):
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)