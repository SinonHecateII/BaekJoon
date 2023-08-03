import sys

N = int(input())

PeopleList = []

for i in range(0, N):
    age, name = map(str, sys.stdin.readline().split())

    PeopleList.append([int(age), name, i])

s_PeopleList = sorted(PeopleList, key = lambda x : (x[0], x[2]))

for i in range(0, N):
    print(str(s_PeopleList[i][0]) + " " + str(s_PeopleList[i][1]))