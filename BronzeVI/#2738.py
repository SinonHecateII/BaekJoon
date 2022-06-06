row, col = input().split()
row, col = int(row), int(col)

arr1 = []
arr2 = []

for i in range(0, row):
    num = list(map(int, input().split()))
    for j in range(0, col):
        arr1[i][j] = int(InputNum[j])

for i in range(0, row):
    for j in range(0, col):
        print(arr1[row][col], end = '')
    print('')
        