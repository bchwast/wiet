#include <stdio.h>
#include <stdlib.h>

int main() {
    unsigned int array_size;
    int num = 1, border = 0;
    scanf("%d", &array_size);
    int n = (int) array_size;

    int **T = (int **)malloc(array_size * sizeof(int *));
    for (int i = 0; i < array_size; i++) {
        T[i] = (int *)malloc(array_size * sizeof(int));
    }

    while (num <= n * n) {
        for (int i = border; i < n - border; i++) {
            T[border][i] = num;
            num++;
        }
        if (num - 1 == n * n) break;

        for (int i = border + 1; i < n - (border + 1); i++) {
            T[i][(n - 1) - border] = num;
            num++;
        }
        if (num - 1 == n * n) break;

        for (int i = (n - 1) - border; i >= border; i--) {
            T[(n - 1) - border][i] = num;
            num++;
        }
        if (num - 1 == n * n) break;

        for (int i = (n - 1) - (border + 1); i > border; i--) {
            T[i][border] = num;
            num++;
        }
        if (num - 1 == n * n) break;

        border++;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", T[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < n; i++) {
        free(T[i]);
    }
    free(T);

    return 0;
}