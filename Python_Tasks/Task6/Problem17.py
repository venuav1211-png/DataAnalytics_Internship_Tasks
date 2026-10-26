# Problem Name: Check Strict Superset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem[cite: 14]

a = set(map(int, input().split()))
n = int(input())
is_strict_superset = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    if not a.issuperset(other_set) or a == other_set:
        is_strict_superset = False

print(is_strict_superset)