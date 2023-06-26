#4, 9, 25, 81, x, 1089
#2^2, 3^2, 5^2, 9^2, 17^2..., 33^2
#n+1, n+1, n+2, n+5, ..., n+27

N = int(input())
#다음 도형의 한변 점의 수 = 한변에 있는 점의 수 + (한 변에 있는 점의 수 - 1)
DotCnt = 2
for i in range(0, N):
    DotCnt = DotCnt + (DotCnt - 1)

print(DotCnt * DotCnt)
