a,b=input().split()
a = int(a)
b = int(b)

sum = a - b
if(sum < 0):
    sum = sum * -1
    print(sum)
else:
    print(sum) 