import numpy as np
from collections import Counter

data = None


# calculate the fuel from each point to the median
# multiply with the number of times each number appears
def getFuelCost_normal(median, counter):
    cost = 0
    for num in counter:
        cost += abs(median - num) * counter[num]
    return cost


# slightly different than above
# because the fuel cost gets higher with each step we need to use range which
# will do exactly that. Then again multiply like above
def getFuelCost_extreme(mean, counter):
    cost = 0
    for num in counter:
        cost += sum(range(abs(mean - num) + 1)) * counter[num]
    return cost


def challenge1():
    x = np.median(data)
    count = Counter(data)
    cost = getFuelCost_normal(x, count)
    print("The cost is", cost, "fuel")


def challenge2():
    x = int(np.mean(data))
    count = Counter(data)
    cost = getFuelCost_extreme(x, count)
    print("The cost is", cost, "fuel")


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        data = np.array([int(y) for y in [x.split(",") for x in f.readlines()][0]])
    challenge2()
