import numpy as np


data = None

entries = ["(", "[", "{", "<"]
exits = [")", "]", "}", ">"]
points = {")": 3, "]": 57, "}": 1197, ">": 25137}


def checkSyntax(line):
    symbols = []
    # go trough every single symbol
    for i in line:
        # add to list if its a entry
        if i in entries:
            symbols.append(i)
        # check if it is a correctly placed exit
        # we can do that by taking (and removing) the last element in our Symbol list
        # and checking if its the correct entry symbol for our i
        # if its not, the bracket is corrupt bc it starts with a different entries f.e. ( but i is } so broken Syntax
        elif i in exits:
            last = symbols.pop()
            bracket = entries[exits.index(i)]
            if last != bracket:
                # print(line, i, last, bracket, sep="  ------  ")
                return points.get(i)
    return 0


points_ch2 = {")": 1, "]": 2, "}": 3, ">": 4}


def autofill():
    scores = []
    for line in data:
        # print(line)
        # we ignore lines that are corrupt
        if checkSyntax(line) == 0:
            fill = []
            # for each symbol we check if its an entry or exit.
            # if its an entry we add the exit part to our stack fill
            # if its an exit we remove the first exit Symbol in fill (Stack - First in Last Out)
            for i in line:
                if i in entries:
                    fill.append(exits[entries.index(i)])
                    # print("new: ", fill, "for", i)
                elif i in exits:
                    # really ugly code but it works
                    fill.reverse()
                    fill.remove(i)
                    fill.reverse()
                    # print("new: ", fill, "for", i)
            fill.reverse()
            score = 0
            # calculate the score for this line and add it to the scores list
            for j in fill:
                score = score * 5 + points_ch2.get(j)
            scores.append(score)
    # sort our scores and get the middle point
    scores.sort()
    return scores[round((len(scores) - 1) / 2)]


def challenge1():
    score = 0
    # go trough every Line and check the Syntax
    for line in data:
        score += checkSyntax(line)
    print("Syntax Error Score: ", score)


def challenge2():
    score = autofill()
    print("Auto Fill Score:", score)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    # print(data)
    challenge2()

