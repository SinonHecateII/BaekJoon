import sys

N = int(input())

Num = []
for i in range(0, N):
    Num.append(int(sys.stdin.readline()))

Num.sort()
print(round(sum(Num) / N))  #산술평균

print(Num[N // 2])  #중앙값

#최빈값
Numdict = {}
for i in range(0, N):
    if(Num[i] in Numdict):
        Numdict[Num[i]] += 1
    else:
        Numdict[Num[i]] = 1
sortedNumdict = sorted(Numdict.items(), key = lambda item: item[1])
mostNum = []
for key, value in Numdict.items():
    if value == sortedNumdict[len(sortedNumdict) - 1][1]:
        mostNum.append(key)
mostNum.sort()
if(len(mostNum) > 1):
    print(mostNum[1])
else:
    print(mostNum[0])

#범위
if(len(Num) == 1):
    print(0)
elif(Num[0] < 0 or Num[N - 1] < 0):
    print(abs(Num[0] - Num[N - 1]))
else:
    print(Num[N - 1] - Num[0])