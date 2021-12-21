

data = None


def challenge1():
    count = 0
    lens = [2, 3, 4, 7]
    for line in data:
        for word in line[1].split(" "):
            if len(word) in lens:
                count += 1
    print(count)


# This was pretty hard in my opinion. Only could do it with the help of the guy that
# posted this https://imgur.com/a/LIS2zZr
def challenge2():
    result = 0
    for line in data:
        num = ""
        segment = {}
        # find the corresponding code for the numbers that we always know of
        for word in line[0].strip(" ").split(" "):
            if len(word) == 2:
                segment[1] = word
            elif len(word) == 4:
                segment[4] = word
            elif len(word) == 3:
                segment[7] = word
            elif len(word) == 7:
                segment[8] = word
        #go trough the graph and follow the lines
        for word in line[1].strip(" ").split(" "):
            print(word)
            if len(word) == 2:
                num += "1"
            elif len(word) == 3:
                num += "7"
            elif len(word) == 4:
                num += "4"
            elif len(word) == 7:
                num += "8"
            #[2,3,5]
            elif len(word) == 5:
                if set(segment[7]).issubset(set(word)):
                    num += "3"
                else:
                    if len(set(word).intersection(segment[4])) == 3:
                        num += "5"
                    else:
                        num += "2"
            #[0,6,9]
            elif len(word) == 6:
                if set(segment[4]).issubset(set(word)):
                    num += "9"
                else:
                    if set(segment[7]).issubset(set(word)):
                        num += "0"
                    else:
                        num += "6"
            print(num)
        result += int(num)
    print(result)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        data = [x.strip().split("|") for x in f.readlines()]
    challenge2()
