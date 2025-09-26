#include <iostream>
#define SIZE 3

double** matrix_multiplication(double MatrA[][SIZE], double MatrB[][SIZE]) {
    double** matrixC = new double*[SIZE];
    for (int i = 0; i < SIZE; ++i) {
        matrixC[i] = new double[SIZE];
    }

    for (int i = 0; i < SIZE; ++i) {            
        for (int j = 0; j < SIZE; ++j) {        
            matrixC[i][j] = 0;
            for (int k = 0; k < SIZE; ++k) {
                matrixC[i][j] += MatrA[i][k] * MatrB[k][j];
            }
        }
    }

    return matrixC;
}



