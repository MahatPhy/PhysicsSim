#include "functions.h"
using namespace std;

double NewtonRaphson:: function(double E){
    double p = pow(10-E,0.5);
    double q = tan(p);
    double r = pow(E,0.5);
    return (p*q)-r;
}

double NewtonRaphson:: dfunction(double E){
    double p = function(E+eps);
    double q = function(E);
    return (p-q)/eps;
}

double NewtonRaphson:: deltax(double E){
    double p = function(E);
    double q = dfunction(E);
    return -(p/q);
}


