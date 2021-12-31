import numpy as np


data = []


# increments every neighbor and the octopus itself
def incrementNeighbors(row, col):
    neighbor_cords = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    for x, y in neighbor_cords:
        nrow = row + x
        ncol = col + y
        if (0 <= nrow <= len(data) - 1) and (0 <= ncol <= len(data[0]) - 1):
            # -1 already flashed this step
            if data[nrow][ncol] != -1:
                data[nrow][ncol] += 1


# Goes trough every Octopus and checks if the level is higher then the max
# if it is change octopus to -1 and increment neighbors
def getFlashes():
    global data
    flashes = 0
    for (row, col), level in np.ndenumerate(data):
        if level > 9:
            data[row][col] = -1
            incrementNeighbors(row, col)
            flashes += 1
    return flashes


# resets every -1 to 0
def resetFlashes():
    for (row, col), level in np.ndenumerate(data):
        if level == -1:
            data[row][col] = 0


# checks if every Octopus has level 0
def checkSynchronized(i):
    if np.all(data == 0):
        print(i + 1, data)
        return True
    return False


# goes trough each steps and calculates total flashes
def calculate(steps):
    global data
    total_flashes = 0
    for i in range(steps):
        data += 1
        while flashes := getFlashes():
            total_flashes += flashes
        resetFlashes()
        checkSynchronized(i)
    print(total_flashes)


# does an infinite amount of steps till it finds the step where every octopus
# has level 0
def findSynchronized():
    global data
    total_flashes = 0
    step = 0
    while True:
        data += 1
        while flashes := getFlashes():
            total_flashes += flashes
        resetFlashes()
        if checkSynchronized(step):
            return
        step += 1


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        temp = f.read().splitlines()
        for line in temp:
            row = []
            for octopus in line:
                row.append(int(octopus))
            data.append(row)
    data = np.array(data)
    print(data)
    # calculate(100)
    findSynchronized()
