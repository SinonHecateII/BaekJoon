#include <stdio.h>

int main() {
    int Num, Sum = 0;
    for (int i = 0; i < 5; i++) {
        scanf_s("%d", &Num);
        Sum += Num;
    }

    printf("%d", Sum);

    return 0;
}