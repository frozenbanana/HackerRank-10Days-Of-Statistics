# The number of tickets purchased by each student for
# the University X vs. University Y football game follows
# a distribution that has a mean = 2.4 and a standard deviation of sigma = 2.0.

# A few hours before the game starts, 100 eager students line up to purchase
# last-minute tickets. If there are only 250 tickets left, what is the probability
# that all 100 students will be able to purchase tickets?

import math

def cdf(x, mean, sigma):
    return 1/2 * (1+math.erf((x-mean)/ (sigma * math.sqrt(2))))


if __name__ == "__main__":
    mean = 2.4
    sigma = 2.0
    nr_eager_students = 100
    tickets_left = 250

    # Adjust mean and sigma for the nr_of_students
    mean_prim = mean * nr_eager_students
    sigma_prim = sigma * math.sqrt(nr_eager_students)

    probability_all_students_buy = cdf(tickets_left, mean_prim, sigma_prim)

    print("{:.4f}".format(probability_all_students_buy))