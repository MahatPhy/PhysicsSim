#include "lagrane_interpolation.h"

void LagrangePolynomial::computeWeights() {
        int n = x_points.size();
        weights.resize(n);
        for (int i = 0; i < n; ++i) {
            double product = 1.0;
            for (int j = 0; j < n; ++j) {
                if (j != i) product *= (x_points[i] - x_points[j]);
            }
            weights[i] = y_values[i] / product;
        }
    }


LagrangePolynomial::LagrangePolynomial(const std::vector<double>& x, const std::vector<double>& y)
        : x_points(x), y_values(y) {
        computeWeights();
    }

std::string LagrangePolynomial::getPolynomialExpression() const {
    int n = x_points.size();
    std::ostringstream poly;
    poly << "P(x) = ";
    for (int i = 0; i < n; ++i) {
        if (i != 0 && weights[i] >= 0) poly << " + ";
        else if (i != 0 && weights[i] < 0) poly << " - ";
        else if (weights[i] < 0) poly << "-";
        poly << std::abs(weights[i]);
        for (int j = 0; j < n; ++j) {
            if (j != i) {
                poly << "*(x - " << x_points[j] << ")";
            }
        }
    }
    return poly.str();
}
