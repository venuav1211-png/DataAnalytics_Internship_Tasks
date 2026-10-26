# Problem Name: Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem[cite: 9]

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
  pass


if __name__ == "__main__":
  n = int(input())
  words = [input().strip() for _ in range(n)]
  word_counts = OrderedCounter(words)

  print(len(word_counts))
  print(*(word_counts.values()))