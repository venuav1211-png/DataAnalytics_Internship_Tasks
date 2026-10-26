# Problem Name: Tuples
# HackerRank Link: https://www.hackerrank.com/challenges/python-tuples/problem[cite: 14]

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))


# Another code for same problem
# n = int(raw_input())
# integer_list = tuple(map(int, raw_input().split()))
# print hash(integer_list)