#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>

#define h 1e-7

using namespace std;

class Runge_Kutta_Four {
    public:
        static double function(double t, double y);
        static double k1(double t, double y);
        static double k2(double t, double y);
        static double k3(double t, double y);
        static double k4(double t, double y);
        static double RK4out(double t, double y);
};
