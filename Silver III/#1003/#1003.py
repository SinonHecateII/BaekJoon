import sys

def count(n):
    Sum0 = [1, 0]
    Sum1 = [0, 1]
    loc = 2
    
    while True:
        nextSum0 = Sum0[0] + Sum0[1]
        nextSum1 = Sum1[0] + Sum1[1]
        if(loc == n):
            return nextSum0 ,nextSum1
        Sum0[0] = Sum0[1]
        Sum1[0] = Sum1[1]
        Sum0[1] = nextSum0
        Sum1[1] = nextSum1
        loc += 1

T = int(input())

for i in range(0, T):
    num = int(sys.stdin.readline())
    if(num == 0):
        print(str(1) + " " + str(0))
    elif(num == 1):
        print(str(0) + " " + str(1))
    else:
        x, y = count(num)
        print(str(x) + " " + str(y))