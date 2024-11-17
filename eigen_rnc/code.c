#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef struct {double real;double imag;} Complex;
Complex add(Complex a, Complex b) {
    Complex result = {a.real + b.real, a.imag + b.imag};
    return result;}
Complex subtract(Complex a, Complex b) {
    Complex result = {a.real - b.real, a.imag - b.imag};
    return result;}
Complex multiply(Complex a, Complex b) {
    Complex result = {a.real * b.real - a.imag * b.imag, a.real * b.imag + a.imag * b.real};
    return result;}
Complex divide(Complex a, Complex b) {
    double denominator = b.real * b.real + b.imag * b.imag;
    Complex result = {(a.real * b.real + a.imag * b.imag) / denominator,
                      (a.imag * b.real - a.real * b.imag) / denominator};
    return result;}
Complex conjugate(Complex a) {
    Complex result = {a.real, -a.imag};
    return result;}
double magnitude(Complex a) {
    return sqrt(a.real * a.real + a.imag * a.imag);}
void multiplyMatrices(Complex **A, Complex **B, Complex **result, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = (Complex){0, 0};
            for (int k = 0; k < n; k++) {
                result[i][j] = add(result[i][j], multiply(A[i][k], B[k][j]));
            }
        }
    }
}
void qrDecompose(Complex **A, Complex **Q, Complex **R, int n) {
    Complex norm;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) Q[i][j] = (Complex){1, 0};
            else Q[i][j] = (Complex){0, 0};
            R[i][j] = (Complex){0, 0};
        }
    }
    for (int i = 0; i < n; i++) {
        norm = (Complex){0, 0};
        for (int j = 0; j < n; j++) {
            Complex term = multiply(A[j][i], conjugate(A[j][i]));
            norm.real += term.real;
        }
        norm.real = sqrt(norm.real);
        for (int j = 0; j < n; j++) {
            Q[j][i] = divide(A[j][i], norm);
        }
        for (int j = i; j < n; j++) {
            for (int k = 0; k < n; k++) {
                R[i][j] = add(R[i][j], multiply(conjugate(Q[k][i]), A[k][j]));
            }
        }
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                A[j][k] = subtract(A[j][k], multiply(Q[j][i], R[i][k]));
            }
        }
    }
}
void qrAlgorithm(Complex **A, Complex *eigenvalues, int n) {
    Complex **Q = (Complex **)malloc(n * sizeof(Complex *));
    Complex **R = (Complex **)malloc(n * sizeof(Complex *));
    Complex **temp = (Complex **)malloc(n * sizeof(Complex *));
    for (int i = 0; i < n; i++) {
        Q[i] = (Complex *)malloc(n * sizeof(Complex));
        R[i] = (Complex *)malloc(n * sizeof(Complex));
        temp[i] = (Complex *)malloc(n * sizeof(Complex));
    }
    for (int iter = 0; iter < 100; iter++) {
        qrDecompose(A, Q, R, n);
        multiplyMatrices(R, Q, temp, n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = temp[i][j];
            }
        }
    }
    for (int i = 0; i < n; i++) {eigenvalues[i] = A[i][i];}
    for (int i = 0; i < n; i++) {free(Q[i]);free(R[i]);free(temp[i]);}
    free(Q);
    free(R);
    free(temp);
}
int main() {
    int n;
    printf("Enter the size of the matrix (n x n): ");scanf("%d", &n);
    Complex **A = (Complex **)malloc(n * sizeof(Complex *));
    for (int i = 0; i < n; i++) {
        A[i] = (Complex *)malloc(n * sizeof(Complex));
    }
    printf("Enter the elements of the matrix (real and imaginary parts):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("A[%d][%d] (real, imag): ", i + 1, j + 1);
            scanf("%lf %lf", &A[i][j].real, &A[i][j].imag);
        }
    }
    Complex *eigenvalues = (Complex *)malloc(n * sizeof(Complex));
    qrAlgorithm(A, eigenvalues, n);
    printf("Eigenvalues of the matrix:\n");
    for (int i = 0; i < n; i++) {
        printf("%lf + %lfi\n", eigenvalues[i].real, eigenvalues[i].imag);
    }
    for (int i = 0; i < n; i++) {free(A[i]);}
    free(A);
    free(eigenvalues);
    return 0;
}
