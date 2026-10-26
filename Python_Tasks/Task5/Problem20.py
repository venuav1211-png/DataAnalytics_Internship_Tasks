# Problem Name: Piling Up!
# HackerRank Link: https://www.hackerrank.com/challenges/piling-up/problem[cite: 13]

from collections import deque

def check_piling_up():
    t = int(input())
    for _ in range(t):
        n = int(input())
        d = deque(map(int, input().split()))
        
        last = float('inf')
        possible = True
        
        while d:
            if d[0] >= d[-1]:
                val = d.popleft()
            else:
                val = d.pop()
                
            if val > last:
                possible = False
                break
            last = val
            
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    check_piling_up()