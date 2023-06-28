import math
num = []
cnt = 0
while True:
    num.append(sorted(list(map(int,input().split()))))

    if(num[cnt][0] == 0 and num[cnt][1] == 0 and num[cnt][2] == 0):
        break
    cnt = cnt + 1

for i in range(0, cnt):
    if(pow(num[i][0], 2) + pow(num[i][1], 2) == pow(num[i][2], 2)):
        print('right')
    else:
        print('wrong')

#<풀면서의 문제점>
#문제에서의 숫자가 예시처럼 정렬해서 주는게 아닌 무작위로 준다는점을 제대로 숙지하지 않아 오래 걸림
#숫자를 정렬 후 직각삼각형인지 확인