import numpy as np


# Get first Winner
def challenge1():
    with open("input.txt", "r") as f:
        data = f.readlines()
    bingo_numbers = [int(x) for x in data[0].split(",")]
    bingo_fields = get_bingo_fields(data)
    get_winner(bingo_numbers, bingo_fields)


# Get Last Winner
def challenge2():
    with open("input.txt", "r") as f:
        data = f.readlines()
    bingo_numbers = [int(x) for x in data[0].split(",")]
    bingo_fields = get_bingo_fields(data)
    get_last_winner(bingo_numbers, bingo_fields)


def get_bingo_fields(data):
    data = data[1:]
    k = True
    while k:
        k = data.remove("\n")
    field = []
    for nums in data:
        temp = []
        for i in nums.split():
            if i.isdigit():
                temp.append(int(i))
        field.append(temp)
    bingo_field = []
    for i in range(0, len(field) - 4, +6):
        temp = [field[i], field[i + 1], field[i + 2], field[i + 3], field[i + 4]]
        bingo_field.append(temp)
    # print(bingo_field)
    return bingo_field


def get_winner(bingo_numbers, bingo_fields):
    bingo_win = bingo_fields.copy()
    for i in bingo_numbers:
        for fields in range(0, len(bingo_fields)):
            for field in range(0, len(bingo_fields[0])):
                try:
                    k = bingo_fields[fields][field].index(i)
                    bingo_win[fields][field][k] = True
                    erg = check_field(bingo_win[fields])
                    if erg:
                        calculate_result(bingo_win[fields], i)
                        return
                except ValueError:
                    pass


def get_last_winner(bingo_numbers, bingo_fields):
    bingo_win = bingo_fields.copy()
    winners = []
    for i in bingo_numbers:
        for j, fields in enumerate(bingo_fields):
            if j in winners:
                continue
            for field in range(0, len(bingo_fields[0])):
                try:
                    k = bingo_fields[j][field].index(i)
                    bingo_win[j][field][k] = True
                    erg = check_field(bingo_win[j])
                    if erg:
                        winners.append(j)
                        if len(winners) == len(bingo_fields):
                            calculate_result(bingo_win[j], i)
                            return
                        break
                except ValueError:
                    pass


def check_field(field):
    for i in range(0, len(field)):
        if field[i][0] == field[i][1] == field[i][2] == field[i][3] == field[i][4] == True:
            # print(field, "BINGO - Waagerecht")
            return True
        if field[0][i] == field[1][i] == field[2][i] == field[3][i] == field[4][i] == True:
            # print(field, "BINGO - Senkrecht")
            return True
    return False


def calculate_result(field, last_num):
    result = 0
    for i in range(0, len(field)):
        for j in range(0, len(field)):
            num = field[i][j]
            if type(num) != bool:
                result += num
    print(result, last_num)
    result *= last_num
    print(result)


if __name__ == '__main__':
    challenge2()
