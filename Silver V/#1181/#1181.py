import sys

N = int(input())

word = []
for i in range(0, N):
    word.append(sys.stdin.readline().strip())

result = list(set(word))
result.sort()
result.sort(key = len)

for i in range(0, len(result)):
    print(result[i])