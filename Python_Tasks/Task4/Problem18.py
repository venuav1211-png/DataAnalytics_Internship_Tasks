# Problem Name: Lists
# HackerRank Link: https://www.hackerrank.com/challenges/python-lists/problem[cite: 9]

if __name__ == "__main__":
  N = int(input())
  lst = []
  for _ in range(N):
    command, *args = input().split()
    args = list(map(int, args))
    if command == "print":
      print(lst)
    else:
      getattr(lst, command)(*args)