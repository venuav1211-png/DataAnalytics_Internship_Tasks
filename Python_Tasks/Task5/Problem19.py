# Problem Name: Merge the Tools!
# HackerRank Link: https://www.hackerrank.com/challenges/merge-the-tools/problem[cite: 13]

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i:i+k]
        seen = ""
        for char in sub:
            if char not in seen:
                seen += char
        print(seen)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)