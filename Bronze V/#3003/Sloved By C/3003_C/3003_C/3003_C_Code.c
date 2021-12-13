#include <stdio.h>

int main() {
    int Piece[6] = { 1, 1, 2, 2, 2, 8 };
    int OwnPiece[6];
    scanf_s("%d %d %d %d %d %d", &OwnPiece[0], &OwnPiece[1], &OwnPiece[2], &OwnPiece[3], &OwnPiece[4], &OwnPiece[5]);

    for (int i = 0; i < 6; i++) {
        printf("%d ", Piece[i] - OwnPiece[i]);
    }

    return 0;
}