# A random variable, X, follows Poisson distribution with mean of 2.5.
# Find the probability with which the random variable X is equal to 5.
import math as m


def poisson(lam, k):
    return (lam**k) * (m.e**-lam) / m.factorial(k)


if __name__ == '__main__':
    lam = float(input())
    k = int(input())
    print("%.3f" % poisson(lam,k))
