N = int(input())

sum = []
Dice = [0, 0, 0]
for i in range(0, N):
    Dice[0], Dice[1], Dice[2] = map(int, input().split())
    Dice.sort()
    if(Dice[0] == Dice[1] and Dice[1] == Dice[2]):
        sum.append(10000 + Dice[0] * 1000)
    elif(Dice[0] != Dice[1] and Dice[1] != Dice[2]):
        sum.append(max(Dice[0], Dice[1], Dice[2]) * 100)
    else:
        if(Dice[0] == Dice[1]):
            sum.append(1000 + Dice[0] * 100)
        elif(Dice[1] == Dice[2]):
            sum.append(1000 + Dice[1] * 100)
print(max(sum))