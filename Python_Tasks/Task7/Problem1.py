# Problem Name: Set .symmetric_difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == '__main__':
    n = int(input())
    set_a = set(map(int, input().split()))
    m = int(input())
    set_b = set(map(int, input().split()))
    
    sym_diff = set_a.symmetric_difference(set_b)
    print(len(sym_diff))