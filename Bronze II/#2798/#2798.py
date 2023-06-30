def FindNum():
    sum = 0
    NearNum = 0
    tmp = 1000000  #M과의 차이
    for i in range(0, len(Num) - 2):
        for j in range(i + 1, len(Num) - 1):
            for k in range(j + 1, len(Num)):
                sum = Num[i] + Num[j] + Num[k]
                if(sum <= M and M - sum < tmp):
                    tmp = M - sum
                    NearNum = sum
                    if(tmp == 0):
                        return NearNum
    return NearNum
                
N, M = map(int, input().split())

Num = []
Num = list(map(int, input().split()))

print(FindNum())