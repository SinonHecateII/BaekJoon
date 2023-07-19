from collections import deque  

while True:
    Sentence = str(input())
    if(Sentence == '.'):
        break
    Isno = 0

    dq = deque([])
    parenthesesOpen = 0  #소괄호 열렸는지
    squarebracketsOpen = 0  #대괄호 열렸는지
    for i in range(0, len(Sentence)):
        if(Sentence[i] == '('):
            parenthesesOpen += 1
            dq.append('p')
        elif(Sentence[i] == '['):
            squarebracketsOpen += 1
            dq.append('s')
        elif(Sentence[i] == ')'):
            parenthesesOpen -= 1
            if(len(dq) != 0 and dq.pop() != 'p'):
                break
        elif(Sentence[i] == ']'):
            squarebracketsOpen -= 1
            if(len(dq) != 0 and dq.pop() != 's'):
                break
        if(parenthesesOpen < 0 or squarebracketsOpen < 0):  #닫히는게 먼저 나오면 즉시 종료
            print('no')
            Isno = 1
            break
    if(parenthesesOpen == 0 and squarebracketsOpen == 0):
        print('yes')
    elif(Isno == 0):
        print('no')