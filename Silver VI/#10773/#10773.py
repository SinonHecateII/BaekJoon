from collections import deque
import sys

K = int(input())

num = deque([])
InputNum = 0
for i in range(0, K):
    InputNum = int(sys.stdin.readline())
    if(InputNum != 0):
        num.append(InputNum)
    else:  #문제에서 수가 있었을때만 0이 입력된다고 하기 때문에 별다른 예외 X
        num.pop()
print(sum(num))