# A manufacturer of metal pistons finds that, on average, 12 %of the pistons they manufacture are rejected
# because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

# 1. No more than 2 rejects?
# 2. At least 2 rejects?


def fact(x):
    return 1 if x == 0 else x * fact(x-1)


def combination(n, x):
    denominator = fact(n)
    nominator = fact(x) * fact(n - x)
    return denominator / nominator


def binomial(x, n, p):
    return combination(n, x) * (p**x) * (1-p)**(n-x)


if __name__ == '__main__':
    likelihood_of_failure, batch_size = list(map(int, input().split()))
    likelihood_of_failure /= 100.0      # make it decimal

    probability_no_more_than_2 = 0.0
    probability_at_least_2 = 0.0

    for i in range(2+1):
        probability_no_more_than_2 += binomial(i, batch_size, likelihood_of_failure)

    for i in range(2, batch_size+1):
        probability_at_least_2 += binomial(i, batch_size, likelihood_of_failure)

    print("%.3f" % probability_at_least_2)
    print("%.3f" % probability_no_more_than_2)
