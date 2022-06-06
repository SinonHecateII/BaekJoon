a, b, c = input().split()
num = [int(a), int(b), int(c)]

if(a == b and b == c):
    print(a * 1000 + 10000)
elif(a == b or b == c or a == c):
    print()