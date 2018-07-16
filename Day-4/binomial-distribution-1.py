# The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth,
# what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters. Then print your result,
# rounded to a scale of 3 decimal places (i.e., 1.234 format).


def fact(x):
    return 1 if x == 0 else x * fact(x-1)


def combination(n, x):
    denominator = fact(n)
    nominator = fact(x) * fact(n - x)
    return denominator / nominator


def binomial(x, n, p):
    return combination(n, x) * (p**x) * (1-p)**(n-x)


if __name__ == '__main__':
    ratio_boy, ratio_girl = list(map(float, input().split(" ")))
    ratio = ratio_boy/(ratio_boy+ratio_girl)

    nr_of_children = 6
    nr_boy = 3
    worst_case_zero_boys = nr_of_children - nr_boy
    proportion = 0.0
    for i in range(worst_case_zero_boys, nr_of_children + 1):
        proportion += binomial(i, nr_of_children, ratio)

    print("%.3f" % proportion)
