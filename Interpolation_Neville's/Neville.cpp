#include "headers.h"

double NevilleInterpolation(int n, double x_vals[], double y_vals[], double x) {


    int i, j;
    double P[n][n]; 

    for (i = 0; i < n; ++i) {
        P[i][i] = y_vals[i];
    }

    for (j = 1; j < n; ++j) {
        for (i = 0; i < n - j; ++i) {
            P[i][i+j] = ((x_vals[i+j] - x) * P[i][i+j-1] + (x - x_vals[i]) * P[i+1][i+j]) / (x_vals[i+j] - x_vals[i]);
        }
    }

    return P[0][n-1];
}