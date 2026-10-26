# Problem Name: Introduction to Sets
# HackerRank Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem[cite: 9]


def average(array):
  distinct_set = set(array)
  return sum(distinct_set) / len(distinct_set)


if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  result = average(arr)
  print(result)