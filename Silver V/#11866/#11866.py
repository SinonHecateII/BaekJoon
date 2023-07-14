N, K = map(int, input().split())

People = [1 for i in range(0, N)]

print("<", end = '')
loc = 0
while sum(People) != 0:
    cnt = 0
    while True:
        if(People[loc] == 1):
            cnt += 1
        if(cnt == K):
            break
        if(loc + 1 < N):
            loc += 1
        else:
            loc = 0
    People[loc] = 0
    if(sum(People) == 0):
        print(str(loc + 1), end = '')
    else:
        print(str(loc + 1) + ", ", end = '')
print(">")

