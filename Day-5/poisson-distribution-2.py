# The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:
# The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88.
# The daily cost of operating  is Ca = 160 + 40*X^2.
# The number of repairs, X, that machine B needs is a Poisson random variable with mean 1.55.
# The daily cost of operating  is Cb = 128 + 40*Y^2.
# Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure
# that they operate like new at the start of each day. Find and print the expected daily cost for each machine.
# Print expected daily cost of machine A and B

from math import exp
from math import factorial


def poisson(lam, k):
    return lam**k * exp(-lam) / factorial(k)


if __name__ == "__main__":
    a,b = list(map(float, input().split()))
    Ca = 160 + 40 * (a + a**2)
    Cb = 128 + 40 * (b + b**2)

    print("%.3f" % Ca)
    print("%.3f" % Cb)
