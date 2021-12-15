# AoC Day 1

def challenge1():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    result = 0
    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i - 1]):
            result += 1
    print(result)


def challenge2():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    result = 0
    for i in range(0, len(lines) - 3):
        sumA = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        sumB = int(lines[i + 1]) + int(lines[i + 2]) + int(lines[i + 3])
        if sumA < sumB:
            result += 1
    print(result)


if __name__ == '__main__':
    challenge2()
