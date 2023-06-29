N = int(input())

if(N == 1):
    print(N)
else:
    for i in range(1, N):
        sum = i
        i2str = str(i)

        if(len(i2str) == 1):
            continue

        for j in range(0, len(i2str)):
            sum = sum + int(i2str[j])
        if(N == sum):
            print(i)
            break
    else:
        print('0')