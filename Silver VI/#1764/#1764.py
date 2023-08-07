import sys

N, M = map(int, input().split())

PeopleD = []  #듣도 못한 사람
PeopleB = []  #보도 못한 사람

for i in range(0, N):
    PeopleD.append(sys.stdin.readline().strip())

for j in range(0, M):
    PeopleB.append(sys.stdin.readline().strip())

Answer = set(PeopleB) & set(PeopleD)

Answer = list(Answer)
Answer.sort()
print(len(Answer))
for i in range(0, len(Answer)):
    print(Answer[i])