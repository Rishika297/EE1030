#include <stdio.h>
int main() {
    float centerX = 0.0f, centerY = 2.1667f; 
    float radius = 2.1667f;                    
    float points[2][2] = { {0.0f, 0.0f}, {2.0f, 3.0f} }; 
    float *center = &centerX;
    float *radiusPtr = &radius;
    float (*pointsPtr)[2] = points; 
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;}
    fprintf(file, "Center: %.4f, %.4f\n", *center, *(center + 1));
    fprintf(file, "Radius: %.4f\n", *radiusPtr);
    fprintf(file, "Points: (%.1f, %.1f), (%.1f, %.1f)\n", 
            pointsPtr[0][0], pointsPtr[0][1], pointsPtr[1][0], pointsPtr[1][1]);
    fclose(file);
    printf("Data written to data.txt successfully.\n");
    return 0;
}

