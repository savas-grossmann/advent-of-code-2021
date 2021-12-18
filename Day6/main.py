import numpy as np
from collections import Counter, defaultdict

start = None


# really slow bc of the 2 loops
def challenge(days):
    cpy = np.copy(start)
    for i in range(0, days):
        cpy = cpy - 1
        temp = cpy
        cpy = np.where(cpy < 0, 6, cpy)
        x = np.sum(temp != cpy)
        if x > 0:
            for j in range(x):
                cpy = np.append(cpy, 8)
            print(cpy)
    print(cpy, len(cpy))


# way faster then the old one. Old one goes trough every single fish but its better to just count
# how many fish are in each state (like 0 to 8) and then just do each state in one operation!
def faster(days):
    # get the starting States
    count = Counter(start)
    for i in range(days):
        # create new empty dict for every day
        helper = defaultdict(int)
        #we go trough every state and check if new fish are born
        for state, numbers in count.items():
            # new fish are born! Reset the fish to 6 days and add new ones to state 8
            if state == 0:
                helper[6] += numbers
                helper[8] += numbers
            # no new fish are born! fish go down one state
            else:
                helper[state - 1] += numbers
            # save new states after day i
            count = helper
    print(count.values(), sum(count.values()), "fish!", sep=" ")


if __name__ == '__main__':
    with open("input.txt", "r") as file:
        f = file.readlines()
        start = np.asarray([[int(y) for y in x.split(",")] for x in f][0])
    faster(256)
