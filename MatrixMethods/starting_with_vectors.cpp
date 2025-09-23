#include <iostream>
#include <vector>
using namespace std;

/*

int main() {

    vector<int> numbers;


    numbers.push_back(10);
    numbers.push_back(20);
    numbers.push_back(30);

    cout << numbers[0] << endl;
    cout << numbers.at(1) << endl;

    cout << "Size: " << numbers.size() << endl;
    for (int x : numbers) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}

*/
int main(){
int rows = 2, cols = 3;

// create 2x3 matrix filled with 0
vector<vector<double>> matrix(rows, vector<double>(cols, 0));

// assign values
matrix[0][0] = 1.1;
matrix[0][1] = 2.2;
matrix[0][2] = 3.3;
matrix[1][0] = 4.4;
matrix[1][1] = 5.5;
matrix[1][2] = 6.6;

// print
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        cout << matrix[i][j] << " ";
    }
    cout << endl;
}
return 0;
}