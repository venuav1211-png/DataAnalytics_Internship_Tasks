# Problem Name: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem[cite: 13]

from collections import Counter

if __name__ == '__main__':
    num_shoes = int(input())
    shoe_sizes = Counter(map(int, input().split()))
    num_customers = int(input())
    
    total_earnings = 0
    for _ in range(num_customers):
        size, price = map(int, input().split())
        if shoe_sizes[size] > 0:
            shoe_sizes[size] -= 1
            total_earnings += price
            
    print(total_earnings)