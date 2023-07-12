from collections import deque

N = int(input())

dq = deque(i for i in range(1, N + 1))
while True:
    if(len(dq) == 1):
        break
    dq.popleft()
    tmp = dq.popleft()
    dq.append(tmp)
print(dq[0])