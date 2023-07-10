N = int(input())

cnt = 0
num = 665

while True:
    if('666' in str(num)):
        cnt += 1
    if(cnt == N):
        break
    num += 1
        
print(num)