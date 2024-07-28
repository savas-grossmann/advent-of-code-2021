import heapq


def task1(danger):
    # setup possible directions and needed queues for A* algorithm
    rows, cols = len(danger), len(danger[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pq = [(danger[0][0], 0, 0)]
    min_cost = [[float('inf')] * cols for _ in range(rows)]
    min_cost[0][0] = danger[0][0]

    while pq:
        cost, row, col = heapq.heappop(pq)

        # check if weve reached the end
        if row == rows - 1 and col == cols - 1:
            print(cost - danger[0][0])
            return cost

        # check all directions we can take
        for drow, dcol in directions:
            nrow, ncol = row + drow, col + dcol
            if 0 <= nrow < rows and 0 <= ncol < cols:
                new_cost = cost + danger[nrow][ncol]
                if new_cost < min_cost[nrow][ncol]:
                    min_cost[nrow][ncol] = new_cost
                    heapq.heappush(pq, (new_cost, nrow, ncol))


def task2(danger):
    # create new map with zeros
    old_Length = len(danger)
    new_length = old_Length * 5
    full = [[0 for _ in range(new_length)] for _ in range(new_length)]

    for y_index, y in enumerate(full):
        for x_index, x in enumerate(y):
            n = danger[y_index % old_Length][x_index % old_Length]
            full[y_index][x_index] = (n + ((y_index // old_Length) + (x_index // old_Length)) - 1) % 9 + 1
    task1(full)


if __name__ == '__main__':
    with open('input.txt') as f:
        danger = []
        for line in f.readlines():
            danger.append([int(i) for i in list(line.strip())])
        task2(danger)
