#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <cmath>

class LagrangePolynomial{
    private:

    std::vector<double> x_points;
    std::vector<double> y_values;
    std::vector<double> weights;

    void computeWeights();

    public:

    LagrangePolynomial(const std::vector<double>& x, const std::vector<double>& y);
    std::string getPolynomialExpression() const;

};