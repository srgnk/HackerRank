#!/bin/python3

import sys

class Graph:
    def __init__(self, n):
        self.size = n
        self.vert = dict.fromkeys([n for n in range(n)])
        for node in self.vert.keys():
            self.vert[node] = {}
        
    def print_graph(self):
        print(self.vert)

    def add_edge(self, x, y, w):
        if not y in self.vert[x].keys() or self.vert[x][y] > w:
            self.vert[x][y] = w
            self.vert[y][x] = w

    def dijkstra(self, graph, start):
        path = [-1] * graph.size
        path[start] = 0
        visited = []
        next_to_visit = {start:0}
        
        while bool(next_to_visit):
            node = min(next_to_visit, key=next_to_visit.get)
            del next_to_visit[node]
            
            for child in graph.vert[node].keys():
                #print("node = {} child = {}".format(node, child))
                
                if not child in visited:
                    temp_path = path[node] + graph.vert[node][child]
                    if path[child] == -1 or path[child] > temp_path:
                        path[child] = temp_path
                        next_to_visit[child] = temp_path
                    
            visited.append(node)
        
        del path[start]
        return path
    
t = int(input().strip())
for a0 in range(t):
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    graph = Graph(n)
    for a1 in range(m):
        x,y,r = input().strip().split(' ')
        x,y,r = [int(x),int(y),int(r)]
        graph.add_edge(x - 1, y - 1, r)
    s = int(input().strip())
    result = graph.dijkstra(graph, s-1)
    print (" ".join(map(str, result)))
