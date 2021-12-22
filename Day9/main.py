import numpy as np


data = None


def challenge1():
    low_points = []
    neighbor_coords = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # Go trough every single element and check the neighbors
    for (row, col), val in np.ndenumerate(data):
        neighbors = getNeighbors(row, col, True)
        if all(neighbor > val for neighbor in neighbors):
            low_points.append(val + 1)
    print(sum(low_points))


# Check True if you want value, False for coordinates
def getNeighbors(row, col, value):
    neighbor_coords = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # Go trough every single element and check the neighbors
    neighbors = []
    for x, y in neighbor_coords:
        nrow = row + x
        ncol = col + y
        # check if its possible to have that neighbor (for example row = 0, col = 0 cant have an neighbor upstairs) so skip that
        if (0 <= nrow <= len(data) - 1) and (0 <= ncol <= len(data[0]) - 1):
            if value:
                neighbors.append(data[nrow][ncol])
            else:
                neighbors.append([nrow, ncol])
    return neighbors


# Challenge 2:
visited = []
basins = []


# Finding the lowest point doesnt matter anymore I believe. Just start from a point and find every connected number.
# Dont visit or add nines. If finished get the next lowest one and start the search from there.
def challenge2():
    low_points = findMins()
    for basin_start in low_points:
        visited.append(basin_start)
        basin = dfs(basin_start)
        basins.append(basin)
    result = sorted(basins, reverse=True)[:3]
    print(result)
    print(result[0] * result[1] * result[2])


def findMins():
    low_points = []
    neighbor_coords = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # Go trough every single element and check the neighbors
    for (row, col), val in np.ndenumerate(data):
        neighbors = getNeighbors(row, col, True)
        # check if every neighbor is bigger then the value, if so add to low points
        if all(neighbor > val for neighbor in neighbors):
            low_points.append([row, col])
    return low_points


# normal Depth First Search. Starting with a low point and then adding every single Point to it in the basin. Dont
#   accept 9s or already visited ones.
def dfs(coord):
    size = 1
    for neighbor in getNeighbors(coord[0], coord[1], False):
        if neighbor not in visited:
            visited.append(neighbor)
            if data[neighbor[0]][neighbor[1]] != 9:
                size += dfs([neighbor[0], neighbor[1]])
    return size


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        data = np.array([list(map(int, x.strip())) for x in f.readlines()])
    challenge2()
