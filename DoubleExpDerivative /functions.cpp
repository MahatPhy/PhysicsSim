#include "functions.h"
using namespace std;

void initialize(double *initial_step, double *x, int *number_of_steps) {
    printf("Read in from screen initial step, x and number of steps\n");
    scanf("%lf %lf %d", initial_step, x, number_of_steps);
    return;
}

void second_derivative(int number_of_steps, double x, double initial_step, double *h_step, double *computed_derivative){
    int counter;
    double h;
    h = initial_step;
    for(counter=0; counter<number_of_steps; counter++){
        h_step[counter] = h;
        computed_derivative[counter] = (exp(x+h)-2.*(exp(x-h)))/(h*h);
        h = h*0.5;
    }
    return;
}

void output(double *h_step, double *computed_derivative, double x, int number_of_steps, ofstream& ofile) {
    int i;
    ofile << "Results: " << endl;
    ofile << setiosflags(ios::showpoint | ios::uppercase);
    for (i = 0; i < number_of_steps; ++i) {
        ofile << setw(15) << setprecision(8) << log10(h_step[i]);
        ofile << setw(15) << setprecision(8) << log10(fabs((computed_derivative[i] - exp(x)) / exp(x))) << endl;
    }
}

