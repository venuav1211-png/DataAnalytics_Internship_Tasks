# Problem Name: Caesar Cipher
# HackerRank Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    result = []
    k = k % 26
    for char in s:
        if char.isupper():
            result.append(chr((ord(char) - 65 + k) % 26 + 65))
        elif char.islower():
            result.append(chr((ord(char) - 97 + k) % 26 + 97))
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)