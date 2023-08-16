import sys
N, M = map(int, input().split())

PW = {}

for i in range(0, N):
    site, Password = map(str, sys.stdin.readline().split())

    PW[site] = Password

for i in range(0, M):
    print(PW[sys.stdin.readline().strip()])