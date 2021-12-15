# day2

def challenge1():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        horizontal = 0
        depth = 0
        for line in lines:
            temp = line.split()
            if temp[0] == "forward":
                horizontal += int(temp[1])
            elif temp[0] == "down":
                depth += int(temp[1])
            else:
                depth -= int(temp[1])
        print(horizontal, "*", depth, "=", horizontal * depth, sep=" ")


def challenge2():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        horizontal = 0
        depth = 0
        aim = 0
        for line in lines:
            temp = line.split()
            if temp[0] == "forward":
                horizontal += int(temp[1])
                depth += int(temp[1]) * aim
            elif temp[0] == "down":
                aim += int(temp[1])
            else:
                aim -= int(temp[1])
        print(horizontal, "*", depth, "=", horizontal * depth, sep=" ")


if __name__ == '__main__':
    challenge2()
