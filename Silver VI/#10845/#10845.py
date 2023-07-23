#문제 10828(스택 문제) 코드 푼거 겹쳐서 거기에 추가
import sys

def push(QueueList, num):
    return QueueList.append(num)

def pop(QueueList):  #큐는 맨 앞에있는거 빼는거
    if(len(QueueList) == 0):
        print('-1')
    else:
        print(QueueList[0])

    QueueList = QueueList[1:len(QueueList)]  
    return QueueList

def size(QueueList):
    print(len(QueueList))

def empty(QueueList):
    if(len(QueueList) == 0):
        print(1)
    else:
        print(0) 
def back(QueueList):  #뒤에있는거 출력
    if(len(QueueList) != 0):
        print(QueueList[len(QueueList) - 1])
    else:
        print(-1)
def front(QueueList):  #앞에있는거 출력
    if(len(QueueList) != 0):
        print(QueueList[0])
    else:
        print(-1)

N = int(input())
QueueList = []

for i in range(0, N):
    command = list(sys.stdin.readline().strip().split(' '))
    
    if(command[0] == 'push'):
        push(QueueList, command[1])
    elif(command[0] == 'pop'):
        QueueList = pop(QueueList)
    elif(command[0] == 'size'):
        size(QueueList)
    elif(command[0] == 'empty'):
        empty(QueueList)
    elif(command[0] == 'back'):
        back(QueueList)
    elif(command[0] == 'front'):
        front(QueueList)