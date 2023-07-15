import sys

N = int(input())

for i in range(0, N):
    Word = sys.stdin.readline()
    IsNotPS = 0
    cntOpen = 0  #괄호 열린 갯수
    for j in range(0, len(Word)):
        if(Word[j] == '('):
            cntOpen += 1
        if(Word[j] == ')' and cntOpen == 0):
            print('NO')
            IsNotPS = 1
            break
        elif(Word[j] == ')' and cntOpen > 0):
            cntOpen -= 1
    if(cntOpen == 0 and IsNotPS == 0):
        print('YES')
    elif(cntOpen > 0):
        print('NO')