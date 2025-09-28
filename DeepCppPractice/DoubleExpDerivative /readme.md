The program computes the second derivative of ( e^x ) using the central difference formula.
It outputs to output.txt the logarithmic step size and relative error.


The code uses a central finite difference method to approximate the second derivative, with ( O(h^2) ) accuracy. It iteratively halves the step size ( h ) to analyze convergence. This is related to numerical methods like Runge-Kutta, which solve ODEs, as both involve error analysis and step-size effects.