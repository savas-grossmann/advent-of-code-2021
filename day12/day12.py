from collections import defaultdict

def task1(path, node, visited):
        if node == "end":
            return 1
        if node.islower() and node in visited:
            return 0
        visited = visited.union({node})
        result = 0
        for i in path[node]:
            result += task1(path, i, visited)
        return result

def task2(path, node, visited, duplicate):
        if node == "end":
            return 1
        if node == "start" and visited:
            return 0
        if node.islower() and node in visited:
            if duplicate is None:
                duplicate = node
            else:
                return 0
        visited = visited.union({node})
        result = 0
        for i in path[node]:
            result += task2(path, i, visited, duplicate)
        return result

def day12():
    path = defaultdict(list)
    with open('test/input.txt', 'r') as f:
        for line in f.readlines():
            a, b = line.split("-")
            path[a.strip()].append(b.strip())
            path[b.strip()].append(a.strip())
    print(task1(path, "start", set()))
    print(task2(path, "start", set(), None))


if __name__ == "__main__":
    day12()
# end main