#include <stdio.h>
void find_u_and_f(float matrix[2][2], float rhs[2], float u[2], float *f) {
    float factor;
    if (matrix[0][0] != 0) {
        factor = matrix[0][0];
        for (int i = 0; i < 2; i++) {
            matrix[0][i] /= factor;
        }
        rhs[0] /= factor;
    }
    factor = matrix[1][0];
    for (int i = 0; i < 2; i++) {
        matrix[1][i] -= factor * matrix[0][i];
    }
    rhs[1] -= factor * rhs[0];
    if (matrix[1][1] != 0) {
        factor = matrix[1][1];
        matrix[1][1] /= factor;
        rhs[1] /= factor;
    }
    u[1] = rhs[1];
    u[0] = rhs[0] - matrix[0][1] * u[1];
    *f = 0;}
int main() {
    float centerX = 0.0f, centerY = 2.1667f;
    float radius = 2.1667f;
    float points[2][2] = { {0.0f, 0.0f}, {2.0f, 3.0f} };
    float *radiusPtr = &radius;
    float matrix[2][2] = {{4, 6}, {0, 1}};
    float rhs[2] = {-13, 0};
    float u[2];
    float f;
    find_u_and_f(matrix, rhs, u, &f);
    printf("u = [%.2f, %.2f]\n", u[0], u[1]);
    printf("f = %.2f\n", f);
    printf("Equation of the circle: 3x^2 + 3y^2 - 13y = 0\n");

    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }
    fprintf(file, "Center: %.4f, %.4f\n", centerX, centerY);
    fprintf(file, "Radius: %.4f\n", *radiusPtr);
    fprintf(file, "Points: (%.1f, %.1f), (%.1f, %.1f)\n", 
            points[0][0], points[0][1], points[1][0], points[1][1]);
    fclose(file);

    printf("Data written to data.txt successfully.\n");
    return 0;
}
