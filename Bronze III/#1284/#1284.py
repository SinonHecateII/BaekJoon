InputNum = []
cnt = 0
#0까지 입렵 받기
while True:
    InputNum.append(input())
    if(InputNum[cnt] == '0'):
        cnt = cnt + 1
        break
    cnt = cnt + 1

for i in range(0, cnt - 1):
    sum = len(InputNum[i]) + 1
    for j in range(0, len(InputNum[i])):
        if(InputNum[i][j] == '1'):
            sum = sum + 2
        elif(InputNum[i][j] == '0'):
            sum = sum + 4
        else:
            sum = sum + 3

    print(sum)
