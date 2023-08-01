import sys

N = int(input())

NumList = []
for i in range(0, N):
    x, y = map(int, sys.stdin.readline().split())
    NumList.append([x ,y])

NumList.sort()
for i in range(0, N):
    print(str(NumList[i][0]) + " " + str(NumList[i][1]))
    