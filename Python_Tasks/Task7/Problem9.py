# Problem Name: Beautiful Binary String
# HackerRank Link: https://www.hackerrank.com/challenges/beautiful-binary-string/problem

import math
import os
import random
import re
import sys

def beautifulBinaryString(b):
    return b.count("010")

if __name__ == '__main__':
    n = int(input().strip())
    b = input()
    result = beautifulBinaryString(b)
    print(result)