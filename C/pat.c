#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int main() {
    // grid pattern
    int n = 5;
    int rows = n - 1;
    int columns = 1 - n;
    for (int i = rows; i > -n; --i) {
        for (int j = Columns; j < n; ++j) {
            int distance = max(abs(i), abs(j));
            printf("%d ", distance + 1);
        }
        puts("");
    }
    return 0;
}