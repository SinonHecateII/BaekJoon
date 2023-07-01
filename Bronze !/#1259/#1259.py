while True:
    Num = list(input())
    ReverseNum = []

    if(Num == ['0']):
        break

    for i in range(len(Num) -1, -1, -1):
        ReverseNum.append(Num[i])

    if(Num == ReverseNum):
        print('yes')
    else:
        print('no')