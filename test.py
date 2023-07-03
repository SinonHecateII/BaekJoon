def IsSeorosu(Num1, Num2):
    for i in range(1, len(Num1)):
        if(Num1[i] in Num2):
            return False
    return True

print(IsSeorosu([1, 25, 5], [1, 15, 3, 5]))