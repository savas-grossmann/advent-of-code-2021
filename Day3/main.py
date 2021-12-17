import numpy as np
from collections import Counter


def challenge1():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        gamma = np.zeros((2, len(lines[0]) - 1))
        for line in range(0, len(lines) - 1):
            for i in range(0, len(lines[0]) - 1):
                print(lines[line][i])
                if int(lines[line][i]) == 0:
                    gamma[0, i] += 1
                elif int(lines[line][i]) == 1:
                    gamma[1, i] += 1
        gamma_string = ""
        epsilon_string = ""
        for i in range(0, len(gamma[0])):
            if gamma[0, i] > gamma[1, i]:
                gamma_string += "0"
                epsilon_string += "1"
            else:
                gamma_string += "1"
                epsilon_string += "0"
        # print(gamma_string, epsilon_string)
        result = int(gamma_string, 2) * int(epsilon_string, 2)
        print(result)


def challenge2():
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")
    oxygen = ""
    co2 = ""
    for i in range(len(lines[0])):
        #break if empty
        if not lines:
            break
        # get the number of times each 0 and 1 are in the position i
        most = Counter([x[i] for x in lines])

        #eliminate the correct numbers from the list
        if most['0'] > most['1']:
            lines = [x for x in lines if x[i] == '0']
        else:
            lines = [x for x in lines if x[i] == '1']
        oxygen = lines[0]
    print(oxygen)

    #same as above but changed when numbers are eliminated (for co2)
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")
    for i in range(len(lines[0])):
        counter = Counter([x[i] for x in lines])

        if counter['0'] > counter['1']:
            lines = [x for x in lines if x[i] == '1']
        else:
            lines = [x for x in lines if x[i] == '0']
        if lines:
            co2 = lines[0]
    print(co2)
    print(int(oxygen, 2) * int(co2, 2))


if __name__ == '__main__':
    challenge2()