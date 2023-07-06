import sys

cnt = int(input())

Num = [0] * 100001

#계수 정렬
#입력 범위만큼 배열을 만들어놓고 해당 위치의 숫자가 몇 번 나오는지 횟수를 기록해
#그 횟수만큼 출력(즉 정렬되서 출력)
for i in range(0, cnt):
    InputNum = int(sys.stdin.readline())
    Num[InputNum] += 1

for i in range(0, 100001):
    if(Num[i] != 0):
        for j in range(0, Num[i]):
            print(i)