num = [0 for i in range(0, 5)]
num[0], num[1], num[2], num[3], num[4] = input().split()

Sum = 0
for i in range(0, 5):
    Sum = Sum + (int(num[i]) ** 2)
    
print(Sum % 10)