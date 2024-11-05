#include <stdio.h>

int main() {
    // Define circle parameters
    float centerX = 0.0f, centerY = 2.1667f;  // Center coordinates
    float radius = 2.1667f;                    // Radius
    float points[2][2] = { {0.0f, 0.0f}, {2.0f, 3.0f} }; // Points on the circle

    // Pointer declarations
    float *center = &centerX;
    float *radiusPtr = &radius;
    float (*pointsPtr)[2] = points; // Pointer to array of points

    // Open the file for writing
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write the circle parameters to the file
    fprintf(file, "Center: %.4f, %.4f\n", *center, *(center + 1));  // Dereferencing pointer
    fprintf(file, "Radius: %.4f\n", *radiusPtr);
    fprintf(file, "Points: (%.1f, %.1f), (%.1f, %.1f)\n", 
            pointsPtr[0][0], pointsPtr[0][1], pointsPtr[1][0], pointsPtr[1][1]);

    // Close the file
    fclose(file);
    printf("Data written to data.txt successfully.\n");

    return 0;
}

