#include <stdio.h>
#include <stdlib.h>
#include <math.h>
// Function to perform matrix multiplication
void multiplyMatrices(double **A, double **B, double **result, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = 0;
            for (int k = 0; k < n; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}
// Function to perform QR decomposition (simplified for any n x n matrix)
void qrDecompose(double **A, double **Q, double **R, int n) {
    double norm;
    // Initialize Q as identity matrix and R as zero matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) Q[i][j] = 1;
            else Q[i][j] = 0;
            R[i][j] = 0;
        }
    }
    // QR decomposition using Gram-Schmidt (for any n x n matrix)
    for (int i = 0; i < n; i++) {
        // Calculate the norm of the column
        norm = 0;
        for (int j = 0; j < n; j++) {
            norm += A[j][i] * A[j][i];
        }
        norm = sqrt(norm);
        // Construct the Q matrix (normalize the column vector)
        for (int j = 0; j < n; j++) {
            Q[j][i] = A[j][i] / norm;
        }
        // Calculate R matrix
        for (int j = i; j < n; j++) {
            for (int k = 0; k < n; k++) {
                R[i][j] += Q[k][i] * A[k][j];
            }
        }
        // Update A for next iteration
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                A[j][k] -= Q[j][i] * R[i][k];
            }
        }
    }
}
// Function to perform the QR algorithm to find eigenvalues
void qrAlgorithm(double **A, double *eigenvalues, int n) {
    double **Q = (double **)malloc(n * sizeof(double *));
    double **R = (double **)malloc(n * sizeof(double *));
    double **temp = (double **)malloc(n * sizeof(double *));
       for (int i = 0; i < n; i++) {
        Q[i] = (double *)malloc(n * sizeof(double));
        R[i] = (double *)malloc(n * sizeof(double));
        temp[i] = (double *)malloc(n * sizeof(double));
    }
    // Iterate to refine A towards a diagonal matrix
    for (int iter = 0; iter < 100; iter++) {
        qrDecompose(A, Q, R, n);
        // Multiply R and Q to get the new A
        multiplyMatrices(R, Q, temp, n);
        // Copy result to A
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = temp[i][j];
            }
        }
    }
    // The eigenvalues are the diagonal elements of A
    for (int i = 0; i < n; i++) {
        eigenvalues[i] = A[i][i];
    }
    // Free dynamically allocated memory for matrices
    for (int i = 0; i < n; i++) {
        free(Q[i]);free(R[i]);free(temp[i]);
    }
    free(Q);free(R);free(temp);
}
int main() {
    int n;
    printf("Enter the size of the matrix (n x n): ");scanf("%d", &n);
    double **A = (double **)malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++) {
        A[i] = (double *)malloc(n * sizeof(double));}
    printf("Enter the elements of the matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("A[%d][%d]: ", i + 1, j + 1);
            scanf("%lf", &A[i][j]);
        }
    }
    // Array to store eigenvalues
    double *eigenvalues = (double *)malloc(n * sizeof(double));
    // Call the QR algorithm function to find eigenvalues
    qrAlgorithm(A, eigenvalues, n);
    // Print the eigenvalues
    printf("Eigenvalues of the matrix:\n");
    for (int i = 0; i < n; i++) {
        printf("%lf\n", eigenvalues[i]);
    }
    // Free dynamically allocated memory for matrix A
    for (int i = 0; i < n; i++) {
        free(A[i]);
    }
    free(A);
    free(eigenvalues);
    return 0;
}
