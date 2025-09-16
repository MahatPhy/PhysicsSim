#include "headers.h"

int main() {
    double x_vals[] = {0, 1, 2};
    double y_vals[] = {1, 2, 4};
    double x = 1.5;
    int n = 3;
    double result = NevilleInterpolation(n, x_vals, y_vals, x);
    cout << "Interpolated value at x =" << result << endl;
    return 0;
}
