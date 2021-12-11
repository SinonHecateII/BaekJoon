X_num = input()

D_num = 0
temp = len(X_num) - 1

for i in range(0, len(X_num)):
    D_num = D_num + (int(X_num[temp], 16) * (16 ** i))
    temp = temp - 1

print(D_num)

"""
Shorter Code (After Solving it)
Use Int Built-in Function

code..
print(int(input(), 16))

"""