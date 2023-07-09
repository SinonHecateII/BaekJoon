import sys

N = int(input())

#여러개 입력받는 경우에는 sys.stdin.readline() 사용하기!
Num = []
for i in range(0, N):
    Num.append(int(sys.stdin.readline()))  

Num.sort()
for i in range(0, N):
    print(Num[i])