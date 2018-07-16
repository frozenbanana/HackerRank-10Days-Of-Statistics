# A large elevator can transport a maximum of 9800 pounds.
# Suppose a load of cargo containing 49 boxes must be transported via the elevator.
# The box weight of this type of cargo follows a distribution with a mean = 205 pounds
# and a standard deviation sigma = 15 pounds.
# Based on this information, what is the probability that all 49 boxes can be safely
# loaded into the freight elevator and transported?
import math


def cdf(x, mean, sigma):
    return 1/2 * (1 + math.erf((x-mean)/(sigma * math.sqrt(2))))


if __name__ == '__main__':
    max_load = 9800
    nr_of_boxes = 49
    mean_box = 205
    sigma_box = 15

    # See hackerank.com/challenges/s10-the-central-limit-theorem-1/tutorial
    # To explain sigma_box_prim = sigma_box * sqrt(nr_of_boxes)
    # and mean_box_prim = mean_box * nr_of_boxes

    mean_box_prim = mean_box * nr_of_boxes
    sigma_box_prim = sigma_box * math.sqrt(nr_of_boxes)

    probability_safe = cdf(max_load, mean_box_prim, sigma_box_prim)

    print("{:.4f}".format(probability_safe))

