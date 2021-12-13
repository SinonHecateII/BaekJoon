L, P = input().split()

Num = [0 for i in range(0, 5)]
Num[0], Num[1], Num[2], Num[3], Num[4] = input().split()

for i in range(0, 5):
    print(int(Num[i]) - (int(L) * int(P)), end = ' ')