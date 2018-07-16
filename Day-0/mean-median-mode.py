import random


def median(lst):
    sortedlst = sorted(lst)
    lstlen = len(lst)
    lower_middle = (lstlen - 1) // 2

    if (lstlen % 2):
        return sortedlst[lower_middle]
    else:
        return (sortedlst[lower_middle] + sortedlst[lower_middle + 1]) / 2.0


N = int(input())
numbers = list(map(int, input().split()))

mean = sum(numbers) / N
median = median(numbers)
mode = max(sorted(numbers), key=numbers.count)

print(mean)
print(median)
print(mode)