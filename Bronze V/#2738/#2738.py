row, col = input().split()
row, col = int(row), int(col)

arr = [[0 for j in range(col)]for i in range(row * 2)]
sumArr = [[0 for j in range(col)]for i in range(row)]

for cycle in range(0, 2):
    for i in range(0, row):
        num = list(map(int, input().split()))
        for j in range(0, col):
            arr[i + (cycle * row)][j] = int(num[j])

for i in range(0, row):
    for j in range(0, col):
        sumArr[i][j] = arr[i][j] + arr[i + row][j]
        print(sumArr[i][j], end = ' ')
    print('')



        