# In a certain plant, the time taken to assemble a car is a random variable, X,
# having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours.
# What is the probability that a car can be assembled at this plant in:
#
# 1. Less than 19.5 hours?
# 2. Between 20 and 22 hours?

import math


def normal_dist(x, mean, variance):
    return 1/2 * (1 + math.erf((x - mean)/ math.sqrt(2*variance)))


if __name__ == "__main__":
    mean, sigma = list(map(int, input().split()))
    less_then = float(input())
    lower_bound, upper_bound = list(map(int, input().split()))

    # 1.
    probabilty_1 = normal_dist(less_then, mean, sigma**2)

    # 2.
    probabilty_2 = normal_dist(upper_bound, mean, sigma**2) - normal_dist(lower_bound, mean, sigma**2)

    print("%.3f" % probabilty_1)
    print("%.3f" % probabilty_2)


