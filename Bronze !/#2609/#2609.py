#최대 공약수
def div(a, b, factor, MinMul):
    cnt = 2
    while True:
        if(a % cnt == 0 and b % cnt == 0):
            a = a // cnt
            b = b // cnt
            factor = factor * cnt
        elif(a % cnt == 0 or b % cnt == 0):
            cnt = cnt + 1
        else:
            aList = soinsu(a, [])
            bList = soinsu(b, [])
            if(IsSeorosu(aList, bList) == True):
                if(MinMul == 1): #만약 최소 공배수 구하는거면 이 함수 이용해서
                    return factor * a * b
                return factor  #서로 서로수이면 끝
            else:
                cnt = cnt + 1

def IsSeorosu(Num1, Num2):
    for i in range(1, len(Num1)):
        if(Num1[i] in Num2):
            return False
    return True

#소인수분해
def soinsu(num, NumList):
    tmp = num
    for i in range(1, tmp):
        for j in range(num // i, 1, -1):
            if(j < i):
                return NumList
            if(i * j < num or num % i != 0):
                break
            if(i * j == num):
                if(i != j):
                    NumList.append(i)
                    NumList.append(j)
                    tmp = j
                    break
                else:
                    NumList.append(i)
                    return NumList
                break
    return NumList

Num1, Num2 = map(int, input().split())

#최대공약수
print(div(Num1, Num2, 1, 0))
print(div(Num1, Num2, 1, 1))