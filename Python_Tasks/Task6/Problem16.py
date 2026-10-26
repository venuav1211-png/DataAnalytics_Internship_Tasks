# Problem Name: Check Subset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-subset/problem[cite: 14]

for _ in range(int(input())):
    a_size = int(input())
    a = set(map(int, input().split()))
    b_size = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))