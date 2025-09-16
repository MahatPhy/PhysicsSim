#include "RungeKutta4.h"

int main() {
    double t0 = 0.0;
    double y0 = 1.0;   // initial condition: y(0) = 1
    double T = 1.0;    // integrate to t=1
    double y = y0;
    int steps = T / h;

    double t = t0;
    for(int i = 0; i < steps; i++) {
        y = Runge_Kutta_Four::RK4out(t, y);
        t += h;
    }

    cout.precision(17);
    cout << "RK4 result at t=1: " << y << endl;
}