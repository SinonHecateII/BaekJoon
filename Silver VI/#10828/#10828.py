import sys

def push(StackList, num):
    return StackList.append(num)

def pop(StackList):
    if(len(StackList) == 0):
        print('-1')
    else:
        print(StackList[len(StackList) - 1])

    StackList = StackList[0:len(StackList) - 1]
    return StackList

def size(StackList):
    print(len(StackList))
N = int(input())
StackList = []

for i in range(0, N):
    command = list(sys.stdin.readline().strip().split(' '))
    
    if(command[0] == 'push'):
        push(StackList, command[1])
    elif(command[0] == 'pop'):
        StackList = pop(StackList)
    elif(command[0] == 'size'):
        size(StackList)
    print(StackList)