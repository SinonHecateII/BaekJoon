# 10828 문제(스택) 문제랑 유사한 부분 코드에 덱 기능 추가
import sys

def push_back(DeckList, num):
    return DeckList.append(num)

def push_front(DeckList, num):
    tmpList = [num]
    return tmpList + DeckList

def pop_back(DeckList):
    if(len(DeckList) == 0):
        print('-1')
    else:
        print(DeckList[len(DeckList) - 1])

    DeckList = DeckList[0:len(DeckList) - 1]
    return DeckList

def pop_front(DeckList):
    if(len(DeckList) == 0):
        print('-1')
    else:
        print(DeckList[0])

    DeckList = DeckList[1:len(DeckList)]
    return DeckList

def size(DeckList):
    print(len(DeckList))

def empty(DeckList):
    if(len(DeckList) == 0):
        print(1)
    else:
        print(0)
def back(DeckList):
    if(len(DeckList) != 0):
        print(DeckList[len(DeckList) - 1])
    else:
        print(-1)

def front(DeckList):
    if(len(DeckList) != 0):
        print(DeckList[0])
    else:
        print(-1)

N = int(input())
DeckList = []

for i in range(0, N):
    command = list(sys.stdin.readline().strip().split(' '))
    
    if(command[0] == 'push_back'):
        push_back(DeckList, command[1])
    elif(command[0] == 'push_front'):
        DeckList = push_front(DeckList, command[1])
    elif(command[0] == 'pop_back'):
        DeckList = pop_back(DeckList)
    elif(command[0] == 'pop_front'):
        DeckList = pop_front(DeckList)
    elif(command[0] == 'size'):
        size(DeckList)
    elif(command[0] == 'empty'):
        empty(DeckList)
    elif(command[0] == 'back'):
        back(DeckList)
    elif(command[0] == 'front'):
        front(DeckList)