import sys

N, K = map(int, sys.stdin.readline().split())

#nCr 계산으로 풀이
#ex) 5C3이면 (5*4*3) // (3*2*1)
Nresult = 1
for i in range(N, N - K, -1):
    Nresult *= i
Kresult = 1
for i in range(K, 0, -1):
    Kresult *= i
if(K == 0):
    print(1)  #nCr에서 K가 0이면 0으로 나누지 않고 결과는 무조건 1
else:
    print(Nresult // Kresult)