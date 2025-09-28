#include <iostream>
#include <cmath>
#include <fstream>
#include "functions.h"
using namespace std;

#define eps 1e-8

double Afunction(double x){
    return pow(x,3)+pow(x,2)-3*x-3; //placeholder
}

double recursive_bisection_method(double min, double max){
    if ((max-min) < eps){
        return (max+min)/2.0;
    }
    double minimum = min;
    double maximum = max;
    double midpoint = (min+max)/2.;

    if (Afunction(max)*Afunction(midpoint) > 0){
        maximum = midpoint;
        return recursive_bisection_method(minimum,maximum);
    }
    else{
        minimum = midpoint;
        return recursive_bisection_method(minimum,maximum);
    }
}