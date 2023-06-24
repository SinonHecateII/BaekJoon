inputNum = int(input())  

Num = list(input().split())

YoungSickPrice = 0
MinSickPrice = 0
for i in range(0, len(Num)):
    #영식 요금제 계산
    if(int(Num[i]) / 30  < 1):
        YoungSickPrice = YoungSickPrice + 10
    elif(int(Num[i]) / 30 >= 1):
        YoungSickPrice = YoungSickPrice + 10 + ((int(Num[i]) / 30) // 1 * 10)
    
    #민식 요금제 계산
    if(int(Num[i]) / 60  < 1):
        MinSickPrice = MinSickPrice + 10
    elif(int(Num[i]) / 60 >= 1):
        MinSickPrice = MinSickPrice + 15 + ((int(Num[i]) / 60) // 1 * 15)
    print(MinSickPrice) 

if(YoungSickPrice > MinSickPrice):

    print('M ' + str(int(MinSickPrice)))
elif(YoungSickPrice == MinSickPrice):
    print('Y M ' + str(int(YoungSickPrice)))
else:
    print('Y ' + str(int(YoungSickPrice)))