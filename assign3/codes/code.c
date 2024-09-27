#include <stdio.h>

int main() {
    int x[] = {1, 0 };
    int y[] = {0, 1 };

    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    
    fprintf(file, "%d %d\n", x[0], y[0]);
    fprintf(file, "%d %d\n", x[1], y[1]);

    fclose(file);

    printf("Coordinates written to data.txt\n");

    return 0;
}

