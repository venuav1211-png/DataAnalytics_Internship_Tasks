# Problem Name: Set .union() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-union/problem[cite: 14]

n = int(input())
set_a = set(map(int, input().split()))
b = int(input())
set_b = set(map(int, input().split()))

print(len(set_a.union(set_b)))