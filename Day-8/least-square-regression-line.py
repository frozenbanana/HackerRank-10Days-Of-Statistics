""" A group of five students enrolls in Statistics immediately after taking a
Math aptitude test. Each student's Math aptitude test score, x, and Statistics
course grade, y, can be expressed as the following list of (x,y) points:
    1. (95, 85)
    2. (85, 95)
    3. (80, 70)
    4. (70, 60)
    5. (60, 70)
If a student scored 80 on the Math aptitude test, what grade would we expect
them to achieve in Statistics? Determine the equation of the best-fit line
using the least squares method, then compute and print the value of y,
when x = 80."""

# Getting values from input()
n = 5
grades = [(95, 85), (85, 95), (80, 70), (70, 65), (60, 70)]

# Finding linear regression Y = a + b * x
X = [x[0] for x in grades]
Y = [y[1] for y in grades]
sum_X = sum(X)
sum_Y = sum(Y)

mean_X = sum_X / n
mean_Y = sum_Y / n

X_2 = sum([x**2 for x in X])
XY = sum([x*y for x,y in zip(X,Y)])

b = (n * XY - sum_X * sum_Y) / (n * X_2 - sum_X**2)
a = mean_Y - b * mean_X

# Answer
result = a + b * 80
print("{:.3f}".format(result))

