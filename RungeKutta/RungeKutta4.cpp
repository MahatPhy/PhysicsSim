#include "RungeKutta4.h"

double Runge_Kutta_Four::function(double t, double y) {
    return pow(y,t); //placeholder
}

double Runge_Kutta_Four::k1(double t, double y){
    return h*(Runge_Kutta_Four::function(t,y));
}

double Runge_Kutta_Four::k2(double t, double y){
    return h*(Runge_Kutta_Four::function(t+h/2,y+(Runge_Kutta_Four::k1(t,y))/2));
}

double Runge_Kutta_Four::k3(double t, double y){
    return h*(Runge_Kutta_Four::function(t+h/2,y+(Runge_Kutta_Four::k2(t,y))/2));
}

double Runge_Kutta_Four::k4(double t, double y){
    return h*(Runge_Kutta_Four::function(t+h,y+(Runge_Kutta_Four::k3(t,y))));
}

double Runge_Kutta_Four::RK4out(double t, double y){
    return (y+(Runge_Kutta_Four::k1(t,y) + 2.0*(Runge_Kutta_Four::k2(t,y)) + 2.0*(Runge_Kutta_Four::k3(t,y)) + Runge_Kutta_Four::k4(t,y))/6.0) ;
}