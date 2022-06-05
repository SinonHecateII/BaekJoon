#include <stdio.h>
#include <string.h>

void PrintSpace(int length, int Col, int IsNum);

int main() {
    char Title[4][15] = { "SHIP NAME", "CLASS", "DEPLOYMENT", "IN SERVICE" };
    char ShipName[5][15] = { "N2 Bomber", "J-Type 327", "NX Cruiser", "N1 Starfighter", "Royal Cruiser" };
    char Class[5][15] = { "Heavy Fighter", "Light Combat", "Medium Fighter", "Medium Fighter", "Light Combat" };
    char Deployment[5][15] = { "Limited", "Unlimited", "Limited", "Unlimited", "Limited" };
    int InService[5] = { 21, 1, 18, 25, 4 };
    int col[3] = { 15, 15, 11};

    for (int i = 0; i < 4; i++) {
        printf("%s", Title[i]);
        PrintSpace(strlen(Title[i]), i, 0);
    }

    for (int i = 0; i < 5; i++) {
        printf("\n");
        printf("%s", ShipName[i]);
        PrintSpace(strlen(ShipName[i]), 0, 0);
        printf("%s", Class[i]);
        PrintSpace(strlen(Class[i]), 1, 0);
        printf("%s", Deployment[i]);
        PrintSpace(strlen(Deployment[i]), 2, 0);
        printf("%d", InService[i]);
        PrintSpace(InService[i], 0, 0);
    }

    return 0;
}

void PrintSpace(int length, int Col, int IsNum) {
    int col[4] = { 15, 15, 11, 10};
    if (IsNum == 1) {
        if (length >= 10) {
            for (int h = 0; h < 8; h++) {
                printf(" ");
            }
        }
        else {
            for (int h = 0; h < 9; h++) {
                printf(" ");
            }
        }
    }
    else {
        for (int h = 0; h < col[Col] - length; h++) {
            printf(" ");
        }
    }
}