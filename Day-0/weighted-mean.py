# Weighted mean is used when you want some datapoint to weigh in more into the average than others.
# Each datapoint is assigned a weight that get multiplied and finally averages over the weights.

# Sample input
# 5
# 10 40 30 50 20
# 1 2 3 4 5

# Sample output
# 32.0


N = int(input())
X = list(map(int, input().split(' ')))
W = list(map(int, input().split(' ')))

if len(X) != len(W):
    print("Datapoints array X and weights array W is not of equal length ")
    exit()
else:
    result = 0;
    for i in range(N):
        result += X[i] * W[i]

    result /= sum(W)
    print(round(result, 1))




