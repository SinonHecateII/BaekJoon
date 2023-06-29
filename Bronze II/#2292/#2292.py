N = int(input())

cnt = 0
N1 = 2
N2 = 7

if(N == 1):  #해당 부분이 만족하면 while문 안에 들어가지 않게 해야되는데 이를 빼먹어 같히는 현상으로 오래걸림
    print('1')
elif(cnt == 0 and N1 <= N and N <= N2):
    print(cnt + 2)
else:    
    while True:
        if(N1 <= N and N <= N2):
            print(cnt + 2)
            break
        else:
            N1 = N1 + (6 * (cnt + 1))
            N2 = N2 + (6 * (cnt + 2))
            cnt = cnt + 1