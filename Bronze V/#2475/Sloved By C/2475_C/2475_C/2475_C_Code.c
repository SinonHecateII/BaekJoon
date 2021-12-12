#include <stdio.h>
#include <math.h>

int main() {
    int num[5];

    scanf_s("%d %d %d %d %d", &num[0], &num[1], &num[2], &num[3], &num[4]);

    int Sum = 0;
    for (int i = 0; i < 5; i++) {
        Sum += pow(num[i], 2);
    }
    printf("%d", Sum % 10);

    return 0;
}