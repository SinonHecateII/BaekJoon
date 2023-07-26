#재귀함수 
""" 백준 기준으로 재귀 깊이로 인해 Recurission Error 발생
def factorial(N):
    if(N == 1):
        return 1
    return N * factorial(N - 1)
"""

def factorial(N):
    result = 1
    for i in range(N, 0, -1):
        result *= i
    return result

N = int(input())
Num2String = str(factorial(N))

cnt = 0
for i in range(len(Num2String) - 1, -1, -1):
    if(Num2String[i] == '0'):
        cnt += 1
    else:
        break
print(cnt)