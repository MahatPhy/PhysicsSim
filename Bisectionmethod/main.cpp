#include "functions.h"
using namespace std;

//example main space

int main(void){
    double a = 0;
    double b = 2;
    double c = recursive_bisection_method(0,2);
    cout << "The output is " << c << endl;
    return 0;
}