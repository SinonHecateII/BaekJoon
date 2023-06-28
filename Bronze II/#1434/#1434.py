#박스 N개가 한줄, 박스에 책 M개

N, M = map(int, input().split())

A = []  #박스의 용량
B = []  #책의 크기
A = list(map(int, input().split()))  #리스트를 숫자로 받기
B = list(map(int,input().split()))

IsLocked = [0 for i in range(N)]

for i in range(0, M):  #책
    for j in range(0, N):  #박스
        if(B[i] <= A[j] and IsLocked[j] == 0):
            A[j] = A[j] - B[i]
            break
        else:
            IsLocked[j] = 1
            continue


print(sum(A))