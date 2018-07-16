# You have a sample of 100 values from a population with mean = 500
# and with standard deviation sigma = 80. Compute the interval
# that covers the middle 95% of the distribution of
# the sample mean; in other words, compute A and B such that P(A<x<B) = 0.95.
# Use the value of z = 1.96. Note that z is the z-score.

import math

def calculate_margin_error(sigma, z, size):
    # standard error is the standard deviation of the sampling distribution
    standard_error = sigma/math.sqrt(size)
    return standard_error * z


if __name__ == "__main__":
    size = 100
    mean = 500
    sigma = 80
    interval_coverage = 0.95
    z = 1.96

    margin_error = calculate_margin_error(sigma, z, size)
    a = mean - margin_error
    b = mean + margin_error

    print("{:.2f}".format(a))
    print("{:.2f}".format(b))

