num = list(map(int, input().split()))
max = 0

if(num[0] == num[1] == num[2]):
    print(10000 + num[0] * 1000)
else:
    if(num[0] == num[1] or num[0] == num[2]):
        print(1000 + num[0] * 100)
    elif(num[1] == num[2]):
        print(1000 + num[1] * 100)
    else:
        for i in range(0, 3):
            if(num[i] > max):
                max = num[i]
        print(max * 100)