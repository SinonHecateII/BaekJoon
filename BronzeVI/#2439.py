n = int(input())
num1 = 0
num2 = 0

for i in range(0, n):
    num1 = n - i - 1
    num2 = i + 1
    print(' ' * num1, end = '')
    print('*' * num2)