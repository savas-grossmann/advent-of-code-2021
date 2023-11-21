def day13(inputPoints, foldLines):
    data = set()
    for axis, foldLine in foldLines:
        if axis == "x":
            inputPoints = {
                (
                    x if x < foldLine else 2 * foldLine - x, y
                )
                for x, y in inputPoints
            }
        elif axis == "y":
            inputPoints = {
                (
                    x, y if y < foldLine else 2 * foldLine - y
                )
                for x, y in inputPoints
            }
    dots = inputPoints
    xmin = min(x for x, y in dots)
    xmax = max(x for x, y in dots)
    ymin = min(y for x, y in dots)
    ymax = max(y for x, y in dots)
    for y in range(ymin, ymax + 1):
        print("".join("#" if (x, y) in dots else " "
                      for x in range(xmin, xmax + 1)))
    print(len(dots))


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        coordinates, fold = [], []
        for line in f.readlines():
            if "," in line:
                coordinates.append((int(line.strip().split(",")[0]), int(line.strip().split(",")[1])))
            elif len(line) == 1:
                continue
            else:
                a = line.strip().split("=")
                fold.append([a[0][len(a[0]) - 1], int(a[1])])
    day13(coordinates, fold)
# end main
