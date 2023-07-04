repeat = int(input())

while repeat != 0:
    NumList = []
    NextFloorList = []
    k = int(input())
    n = int(input())

    for i in range(0, n):
        NumList.append(i + 1)
        NextFloorList.append(0)

    for floor in range(0, k):
        for Nowroom in range(0, n):
            NextFloorList[Nowroom] = 0
            for Lowroom in range(0, Nowroom + 1):
                NextFloorList[Nowroom] = NextFloorList[Nowroom] + NumList[Lowroom]
        for j in range(0, n):
            NumList[j] = NextFloorList[j]
    print(NextFloorList[n - 1])
    repeat = repeat - 1