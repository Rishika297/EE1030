#include <stdio.h>

int main() {
    int x[] = {-2, 6, 8, 0};
    int y[] = {3, 7, 3, -1};

    FILE *file = fopen("parallelogram_coordinates.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    
    fprintf(file, "A(%d, %d)\n", x[0], y[0]);
    fprintf(file, "B(%d, %d)\n", x[1], y[1]);
    fprintf(file, "C(%d, %d)\n", x[2], y[2]);
    fprintf(file, "D(%d, %d)\n", x[3], y[3]);

    // Close the file
    fclose(file);

    printf("Coordinates written to parallelogram_coordinates.txt\n");

    return 0;
}

