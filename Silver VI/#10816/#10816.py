N = int(input())

NumCard = []
NumCard = list(map(int, input().split()))

M = int(input())
Num2Find = []
Num2Find = list(map(int, input().split()))

Num = {}
for i in range(0, M):
    Num[Num2Find[i]] = 0

for i in range(0, N):
    if NumCard[i] in Num:
        Num[NumCard[i]] += 1

for i in range(0, M):
    print(Num[Num2Find[i]], end = ' ')