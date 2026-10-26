# Problem Name: Designer Door Mat
# HackerRank Link: https://www.hackerrank.com/challenges/designer-door-mat/problem[cite: 14]

if __name__ == '__main__':
    n, m = map(int, input().split())
    # Top pattern
    for i in range(1, n, 2):
        print((".|." * i).center(m, '-'))
    # Welcome line
    print("WELCOME".center(m, '-'))
    # Bottom pattern
    for i in range(n - 2, 0, -2):
        print((".|." * i).center(m, '-'))