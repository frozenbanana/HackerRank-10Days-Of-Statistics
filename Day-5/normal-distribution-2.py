# The final grades for a Physics exam taken by a large group of students have
# a mean = 70 and a standard deviation of sigma = 10.
# If we can approximate the distribution of these grades by a normal distribution,
# what percentage of the students:

# Scored higher than 80?
# Passed the test (60>=)?
# Failed the test (<60)?
import math


def normal_distribution(x, mean, sigma):
    return 0.5*(1 + math.erf((x-mean)/(sigma * math.sqrt(2))))


if __name__ == "__main__":
    mean = 70
    sigma = 10

    # x parameter will give cumulative probability < x
    scored_higher = 1 - normal_distribution(80, mean, sigma)
    passed = 1 - normal_distribution(60, mean, sigma)
    failed = normal_distribution(60, mean, sigma)

    print("{:.2f}".format(scored_higher * 100))
    print("{:.2f}".format(passed * 100))
    print("{:.2f}".format(failed * 100))
