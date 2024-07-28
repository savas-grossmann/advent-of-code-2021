from collections import Counter
from collections import defaultdict


def task1(word, template):
    # too slow for 40 iterations
    for i in range(10):
        temp = word
        hit = 0
        for j in range(0, len(word) - 1):
            key = word[j] + word[j + 1]
            if key in template:
                hit += 1
                temp = temp[:j + hit] + template.get(key) + temp[j + hit:]
        word = temp
    counter = Counter(word)
    lowest = min(counter, key=counter.get)
    highest = max(counter, key=counter.get)
    print(counter[highest] - counter[lowest])


def task2(word, template):
    counter = defaultdict(int)
    # get all pairs in starting word with count = 1
    for i in range(len(word) - 1):
        counter[word[i: i + 2]] += 1

    for _ in range(40):
        next_counter = defaultdict(int)
        # go through all found pairs in counter
        for key, value in counter.items():
            # for each pair find the newly created pairs and add the val
            # Example: counter{NN: 1} , with template NN -> A, so next{NA: 1, AN: 1}
            next_counter[key[0] + template[key]] += value
            next_counter[template[key] + key[1]] += value
        counter = next_counter

    # count how many times each letter is in final counter dict
    single = defaultdict(int)
    for key, value in counter.items():
        single[key[0]] += value
    single[word[-1]] += 1

    # sort and print highest - lowest
    singles = sorted(y for x, y in single.items())
    print(singles[-1] - singles[0])


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        start = lines[0].strip()
        codes = lines[2::]
        formatted = {}
        for code in codes:
            code = code.strip().split("->")
            formatted[code[0].strip()] = code[1].strip()
        # task1(start, formatted)
        task2(start, formatted)