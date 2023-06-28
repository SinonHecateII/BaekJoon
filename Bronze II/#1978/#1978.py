num = []
cnt = int(input())
num = list(map(int, input().split()))

total = 0
for i in range(0, cnt):
    check = 0
    if(num[i] == 1):
        continue
    for j in range(2, num[i]):
        if(num[i] % j == 0):
            check = 1
    if(check == 0):
        total = total + 1
print(total)