#include "functions.h"
#include <fstream>
using namespace std;

int main(void){
    ofstream outfile("data.dat");
    double E = 0.0;
    int iter = 0;
    do{
        iter++;
        outfile << iter << " " << E;
        E = E + NewtonRaphson::deltax(E)*lr;
    } while(NewtonRaphson::function(E) > lr);

    outfile.close();

    cout << E << "is the number" << endl;
    return 0;
}