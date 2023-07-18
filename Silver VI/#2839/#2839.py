N = int(input())

cntBag = 0
while N > 0:
    if(N % 5 == 0):
        cntBag += N // 5
        print(cntBag)
        break
    else:
        N -= 3
        cntBag += 1
    if(N == 0):
        print(cntBag)
if(N < 0):
    print(-1)