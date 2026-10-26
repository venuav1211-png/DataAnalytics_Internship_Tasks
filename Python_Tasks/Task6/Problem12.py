# Problem Name: Set .discard(), .remove() & .pop()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem[cite: 14]

n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    parts = input().split()
    command = parts[0]
    if command == "pop":
        if s:
            s.pop()
    elif command == "remove":
        s.remove(int(parts[1]))
    elif command == "discard":
        s.discard(int(parts[1]))

print(sum(s))