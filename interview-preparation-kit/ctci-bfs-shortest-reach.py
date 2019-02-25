# TESTING
import queue

class Graph:
    def __init__(self, n):
        self.size = n
        self.vert = dict.fromkeys([n for n in range(n)])
        for node in self.vert.keys():
            self.vert[node] = []
        
    def print_graph(self):
        print(self.vert)

    def connect(self, x, y):
        self.vert[x].append(y)
        self.vert[y].append(x)
        
    def find_shortest(self, start):
        next_to_visit = queue.Queue()
        visited = []
        node = start
        next_to_visit.put(node)
        distances = [-1] * self.size
        distances[node] = 0
        
        while not next_to_visit.empty():
            node = next_to_visit.get()
            height = distances[node]
           
            for adj in self.vert[node]:
                if not adj in visited:
                    distances[adj] = height + 6
                    next_to_visit.put(adj)
                    visited.append(adj)
        return distances
        
    def find_all_distances(self, start):
        result = self.find_shortest(start)
        for ind, node in enumerate(result):
            if ind != start:
                print("{} ".format(node), end='')
        print()
            

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    #graph.print_graph()
    graph.find_all_distances(s-1)