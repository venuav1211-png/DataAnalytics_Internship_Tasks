# Problem Name: String Split and Join
# HackerRank Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem[cite: 9]


def split_and_join(line):
  return "-".join(line.split(" "))


if __name__ == "__main__":
  line = input()
  result = split_and_join(line)
  print(result)