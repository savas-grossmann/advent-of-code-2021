# import numpy as np
from collections import defaultdict


def getVents():
    #get the input in nice Lists
    lines = [x.strip() for x in f]
    output = defaultdict(int)
    output_diags = defaultdict(int)

    for line in lines:
        #split by -> and save the correct coordinates as ints in x1 etc.
        start, end = line.split("->")
        # print(start, end)
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        #calculate distances
        distance_x = x2 - x1
        distance_y = y2 - y1

        #i stands for the differences like 0,1 -> 0,4: i is 0,1 - 0,2 - 0,3 - 0,4 etc.
        for i in range(0, 1 + max(abs(distance_x), abs(distance_y))):
            # calculate the correct coordinate
            x = x1 + (1 if distance_x > 0 else (-1 if distance_x < 0 else 0)) * i
            y = y1 + (1 if distance_y > 0 else (-1 if distance_y < 0 else 0)) * i
            # print(x, y)
            # challenge 1 doesnt want Diagonal lines so we only save straight ones
            if distance_x == 0 or distance_y == 0:
                output[(x, y)] += 1
            output_diags[(x, y)] += 1

    # go trough our dicts and sum all Coordinates with more then one hit
    print(len([x for x in output if output[x] > 1]))
    print(len([x for x in output_diags if output_diags[x] > 1]))


if __name__ == '__main__':
    with open("input.txt", "r") as file:
        f = file.readlines()
    getVents()
