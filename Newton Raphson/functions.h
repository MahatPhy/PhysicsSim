#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;

#define eps 1e-6
#define lr 1e-3

class NewtonRaphson {
    private:
        double E;
    public:
        static double function(double E);
        static double dfunction(double E);
        static double deltax(double E);
};

