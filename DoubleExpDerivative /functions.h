#include <iostream>
#include <cmath>
#include <fstream>
#include <iomanip>

using namespace std;

void initialize(double*, double*, int*);
void second_derivative(int, double, double, double*, double*);
void output(double*, double*, double, int, std::ofstream&);
