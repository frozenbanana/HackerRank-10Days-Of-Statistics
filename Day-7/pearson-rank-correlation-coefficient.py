n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))


def rank_list(l):
    rank_list = []
    n = len(l)
    rank = 1
    for i in range(n):
        # Determine rank for element in l
        current_element = l[i]
        for j in range(n):
            if current_element > l[j]:
                rank += 1
        rank_list.append(rank)
        rank = 1

    return rank_list


r_x = rank_list(X)
r_y = rank_list(Y)
d = [rx - ry for rx,ry in zip(r_x,r_y)]
d_2 = [d_**2 for d_ in d]

for i in range(0,n):
    print("X[" + str(i)+"]: " + str(X[i]), end=" | ")
    print("Y[" + str(i)+"]: " + str(Y[i]), end=" | ")
    print("d: " + str(d[i]), end=" | ")
    print("d^2: " + str(d_2[i]))


spearman_rank_correlation_coefficient = 1 - (6 * sum(d_2)) / (n*(n**2-1))

print("{:.3f}".format(spearman_rank_correlation_coefficient))


