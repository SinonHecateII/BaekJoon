Piece = [1, 1, 2, 2, 2, 8]
OwnPiece = [0 for i in range(0, 6)]

OwnPiece[0], OwnPiece[1], OwnPiece[2], OwnPiece[3], OwnPiece[4], OwnPiece[5] = input().split()

for i in range(0, 6):
    print(int(Piece[i]) - int(OwnPiece[i]), end = ' ')