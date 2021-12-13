#include <stdio.h>

int main() {
    int L, P;
    scanf_s("%d %d", &L, &P);

    int Num[5];
    scanf_s("%d %d %d %d %d", &Num[0], &Num[1], &Num[2], &Num[3], &Num[4]);

    for (int i = 0; i < 5; i++) {
        printf("%d ", Num[i] - (L * P));
    }

    return 0;
}