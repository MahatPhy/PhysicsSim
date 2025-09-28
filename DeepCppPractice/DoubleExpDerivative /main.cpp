#include "functions.h"
ofstream ofile;

int main(int argc, char* argv[]){
    char* outfilename;
    int number_of_steps;
    double x, initial_step;
    double *h_step, *computed_derivative;

    if(argc <= 1){
        cout << "Bad usage: " << argv[0] << "read also output file on same line" << endl;
    exit(1);
    }
    else{
        outfilename = argv[1];
    }
    ofile.open(outfilename);
    initialize(&initial_step,&x,&number_of_steps);
    h_step = new double[number_of_steps];
    computed_derivative = new double[number_of_steps];
    second_derivative(number_of_steps,x,initial_step,h_step,computed_derivative);
    output(h_step,computed_derivative,x,number_of_steps, ofile);
    delete[] h_step;
    delete[] computed_derivative;
    ofile.close();
    return 0;
}