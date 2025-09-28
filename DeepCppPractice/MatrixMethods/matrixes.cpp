#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

#define SIZE 3

double** Gaussian_Elimination(double** matrix);

int main(){
    srand(14);
    double** matrix_rows = new double*[SIZE];
    for(int i = 0; i< SIZE; i++){
        double* matrix_cols = new double[SIZE];
        matrix_rows[i] = matrix_cols;
    }

    for(int i = 0; i < SIZE; i++){
        for(int j = 0; j < SIZE; j++){
            matrix_rows[i][j] = rand()%10;
            if(i == j){
                matrix_rows[i][j] = 1;
            }
        }
    }
    double** U = Gaussian_Elimination(matrix_rows);
    
    for(int i = 0; i < SIZE; ++i){
        cout << "row" << i+1 <<endl;
        for (int j = 0; j < SIZE; ++j){
            cout << matrix_rows[i][j] << " ";
        }
        cout << endl;
    }
    
        
    for(int i = 0; i < SIZE; ++i){
        delete[] matrix_rows[i];
        matrix_rows[i] = nullptr;
    }

    delete[] matrix_rows;
    matrix_rows = nullptr;
    return 0;
}

double** Gaussian_Elimination(double** matrix){
    double** matrix_row_gauss = new double*[SIZE];

    for(int i = 0; i < SIZE; ++ i){
        double* matrix_column_gauss = new double[SIZE];
        matrix_row_gauss[i] = matrix_column_gauss;
    }
    for(int i = 0; i < SIZE; ++i){
        for(int j = 0; j< SIZE; ++j){
            if(i == j){
                matrix_row_gauss[i][j] = 1;
            }
            if(j > i){
                matrix_row_gauss[i][j] = 0;
            }
            else{
                matrix_row_gauss[i][j] = matrix[i][j];
            }
            
        }
    }

    for (int k = 0; k < SIZE; ++k) {          
        for (int i = k+1; i < SIZE; ++i) {    
            double factor = matrix_row_gauss[i][k] / matrix_row_gauss[k][k];
                for (int j = k; j < SIZE+1; ++j) {
                    matrix_row_gauss[i][j] -= factor * matrix_row_gauss[k][j];
                    cout << matrix_row_gauss[i][j] << " ";
                }
                cout << endl;
        }
    }


    return matrix_row_gauss;
}