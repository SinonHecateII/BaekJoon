import sys

PokemonDict = {}

N, M = map(int, input().split())

for i in range(0, N):
    PokemonDict[sys.stdin.readline().strip()] = i + 1

reversePokemonDict = {v:k for k, v in PokemonDict.items()}

for i in range(0, M):
    InputQ = sys.stdin.readline().strip()
    if InputQ.isdigit():
        print(reversePokemonDict.get(int(InputQ)))
    else:
        print(PokemonDict.get(InputQ))