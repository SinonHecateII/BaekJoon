import sys

N = int(input())
A = []
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(input())
NumList = []
NumList = list(map(int, sys.stdin.readline().split()))

#이진 탐색

for i in range(0, len(NumList)):
    IsFind = 0
    left = 0
    right = N - 1
    while left <= right:
        middle = (left + right) // 2
        if(NumList[i] == A[middle]):
            IsFind = 1
            print(1)
            break
        elif NumList[i] > A[middle]:
            left = middle + 1
        else:
            right = middle - 1
    if(IsFind == 0):
        print(0)