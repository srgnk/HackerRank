#!/usr/bin/env python3

import queue

class Cell:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

def point_is_valid(horse, size):
    if any(x < 1 for x in horse) or any(x > size for x in horse):
        return False
    else:
        return True

def print_path(init, parent):
    tup = (init[0], init[1])
    if tup in parent.keys():
        prev = parent[tup]
        print_path((prev[0], prev[1]), parent)
    print(tup, end=' ')


def find_path_dijkstra(horse, king, size, a, b):
    res_dist = -1
    next_to_visit = {(horse[0], horse[1]):0}
    distances = [[-1] * (size + 1) for _ in range(size + 1)]
    distances[horse[0]][horse[1]] = 0
    parent = {}
    directions = [[a, b], [b, a], [a, -b], [b, -a], [-a, b], [-b, a], [-a, -b], [-b, -a]]
    #print("solving for: ({}, {})".format(a, b))

    while bool(next_to_visit):
        c = min(next_to_visit, key=next_to_visit.get)
        del next_to_visit[c]

        if c[0] == king[0] and c[1] == king[1]:
            res_dist = distances[c[0]][c[1]]
            break

        for di in directions:
            # child
            x, y = c[0] + di[0], c[1] + di[1]

            if point_is_valid([x, y], size) and distances[x][y] == -1:
                temp_path = distances[c[0]][c[1]] + 1
                if distances[x][y] == -1 or distances[x][y] > temp_path:
                    distances[x][y] = temp_path
                    next_to_visit[(x, y)] = temp_path
                    parent[(x, y)] = [c[0], c[1]]

    #for i in range(1, size + 1):
    #    print(" ".join(map(str, distances[i][1:])))

    #print_path(king, parent)
    #print()

    return res_dist

if __name__ == "__main__":
    board_size = int(input().strip())
    horse = [1, 1]
    king = [board_size, board_size]

    for a in range(1, board_size):
        for b in range(1, board_size):
            print("{}".format(find_path_dijkstra(horse, king, board_size, a, b)), end = ' ')
        print()
