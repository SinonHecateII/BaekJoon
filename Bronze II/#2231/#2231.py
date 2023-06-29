N = int(input())

for i in range(1, N + 1):
    sum = i
    i2str = str(i)

    if(i == N):  #이 부분때문에 해결하는데 오래걸림
        print('0')
        break

    for j in range(0, len(i2str)):
        sum = sum + int(i2str[j])
    if(N == sum):
        print(i)
        break