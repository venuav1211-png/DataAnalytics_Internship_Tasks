# Problem Name: Set .add()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-add/problem[cite: 13]

if __name__ == '__main__':
    n = int(input())
    country_stamps = set()
    for _ in range(n):
        country_stamps.add(input())
    print(len(country_stamps))