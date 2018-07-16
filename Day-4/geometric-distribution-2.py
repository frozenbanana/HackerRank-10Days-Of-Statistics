# The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect is found during the first 5 inspections?
from math import factorial


def biomial_neg(x, n, p):
    comb = factorial(n-1)/(factorial(x) * factorial(n-x))
    return comb * p**x * (1-p)**(n-x)


if __name__ == '__main__':
    pd, pn = list(map(int, input().split()))
    size = int(input())
    p = pd/pn
    probability = sum([biomial_neg(1, i, p) for i in range(1, size+1)])
    print("%.3f" % probability)