M, N = map(int, input().split())

for i in range(M, N + 1):
    if(i == 1):
        continue
    #i의 제곱근까지 for문. 그 이상의 더 이상 의미 X
    for j in range(2, int(i ** 0.5) + 1):  
        if(i % j == 0):
            break
    else:
        print(i)
    