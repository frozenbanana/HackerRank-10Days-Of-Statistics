# Given two n-element data sets, X and Y, calculate
# the value of the Pearson correlation coefficient.

import math

def cov(X,Y, mean_x, mean_y):
    sum = 0
    for x,y in zip(X,Y):
            sum += (x - mean_x) * (y - mean_y)

    return sum/len(X)


def get_sigma(arr, mean):
    sum = 0
    for x in arr:
        sum += (x - mean)**2

    return math.sqrt(sum/len(arr))

def pearson(X, Y, mean_x, mean_y):
    sigma_x = get_sigma(X, mean_x)
    sigma_y = get_sigma(Y, mean_y)
    return cov(X, Y, mean_x, mean_y)/(sigma_x*sigma_y)


if __name__ == "__main__":
    size = int(input())
    X = list(map(float, input().split()))
    Y = list(map(float, input().split()))

    mean_x = sum(X)/size
    mean_y = sum(Y)/size
    result = pearson(X, Y, mean_x, mean_y)

    print("{:.3f}".format(result))