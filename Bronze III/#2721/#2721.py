def T(k):
    sum = 0
    for i in range(1, k + 1):
        sum = sum + i
    return sum

cnt = int(input())
W = []
for i in range(0, cnt):
    SamGakSu = 0

    num = int(input())
    for j in range(1, num + 1):
        SamGakSu = SamGakSu + j * T(j + 1)
    W.append(SamGakSu)

for i in range(0, cnt):
    print(W[i])

