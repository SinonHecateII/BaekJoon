N = int(input())
#다음 도형의 한변 점의 수 = 한변에 있는 점의 수 + (한 변에 있는 점의 수 - 1)
DotCnt = 2
for i in range(0, N):
    DotCnt = DotCnt + (DotCnt - 1)

print(DotCnt * DotCnt)