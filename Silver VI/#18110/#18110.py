import sys

def NumRound(num):  #사사오입 반올림
    if(num % 1 >= 0.5):
        return int(num) + 1
    else:
        return int(num)
    
n = int(input())

if n:
    num = []
    for i in range(0, n):
        num.append(int(sys.stdin.readline()))

    num.sort()
    SliceNum = num[NumRound(len(num) * 0.15) : n - NumRound(len(num) * 0.15)]

    print(NumRound(sum(SliceNum) / len(SliceNum)))
else:
    print(0)
#round() 함수를 그냥 사용할경우 부동소수점 오류로 인해 다른 방법이 필요
# 제안1: 사사오입 반올림. 값이 .5 이상일경우 다 올리는거