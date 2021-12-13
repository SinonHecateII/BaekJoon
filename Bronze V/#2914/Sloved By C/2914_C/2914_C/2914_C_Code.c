#include <stdio.h>

int main() {
    float A, I;
    scanf_s("%f %f", &A, &I);

    I = I - 1 + 0.001;
    printf("%.0f", ((A * I / 1) + 1));

    return 0;
}