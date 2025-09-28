#include <iostream>
#include <cmath>

class Legendre{
    public:
        double P(int n, double x){
            if(n==0) return 1;
            if(n==1) return x;
            return ((2*n-1)*x*P(n-1,x)-(n-1)*P(n-2,x))/n;
        }
        double dP(int n, double x){
            return n/(x*x-1)*(x*P(n,x)-P(n-1,x));
        }
    };

    