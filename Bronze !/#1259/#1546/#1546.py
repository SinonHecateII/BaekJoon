N = int(input())

Score = []
Score = list(map(int, input().split()))

M = max(Score)
Sum = 0
for i in range(0, N):
    Sum = Sum + Score[i] / M * 100

print(Sum / N)