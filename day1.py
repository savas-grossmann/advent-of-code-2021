def task1():    
    with open('input.txt', 'r') as f:
        inventory = [x for x in f.read().strip().split("\n")]
        elves = []
        calories = 0
        for i in inventory:
            if i == '':
                elves.append(calories)
                calories = 0
            else:
                calories += int(i)
        print(max(elves))
        return elves

def task2():
    inventory = task1()
    total = 0
    #NOTE: ugly
    #for i in range(3):
    #    calories = max(inventory)
    #    inventory.remove(calories)
    #    total += calories
    #NOTE: better looking
    total = sum(sorted(inventory, reverse=True)[0:3])
    print(total)

if __name__ == "__main__":
    task1()
    task2()
# end main