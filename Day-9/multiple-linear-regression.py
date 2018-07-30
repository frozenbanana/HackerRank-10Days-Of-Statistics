"""Andrea has a simple equation:

            Y = a + b1 * f1 + b1 * f2 + ... + bm * fm

for (m+1) real constants (a, f1, f2, ..., fm). We can say that the value of Y
depends on q features. Andrea studies this equation for n different feature
sets (f1, f2, f3, ..., fm) and records each respective value of Y. If she has
q new feature sets, can you help Andrea find the value of Y for each of the
sets?  Note: You are not expected to account for bias and variance trade-offs.
"""
import numpy

m,n = map(int, input().split())

X = [] 
Y = []
for i in range(n):
    features_and_y = list(map(float, input().split()))
    X.append(features_and_y[:m])   # all elements up to m is part of X
    Y.append(features_and_y[m:])   # the last element is the Y value

q = int(input().strip())
X_new = []

for i in range(q):
    X_new.append(list(map(float, input().split())))

# Type cast lists to numpy array
X = numpy.array(X, float)
Y = numpy.array(Y, float)
X_new = numpy.array(X_new, float)

# Center
Xc = X-numpy.mean(X, axis=0)
Yc = Y-numpy.mean(Y)

# Finding B-matrix
# Knowing that Y = X * B
# Then B = inv(X) * Y if symmetrical
# Otherwise X^t * Y = X^t * X * B
# B = inv(X^t * X) * X^t * Y

B = numpy.linalg.inv(Xc.T.dot(Xc)).dot(Xc.T).dot(Yc)

# Predict
Xc_new = X_new - numpy.mean(X, axis=0)
Yc_new = Xc_new.dot(B)
Y_new = Yc_new + numpy.mean(Y)

# print
for i in Y_new:
    print(round(float(i),2))
