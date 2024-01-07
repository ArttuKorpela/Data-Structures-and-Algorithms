import math


class Graph:

    def __init__(self, n):
        self.n = n
        self.graph_matrix = [[math.inf] * n for i in range(n)]
        self.parent = [i for i in range(n)]
        self.connections = []



    def add(self, u, v):
        if u < self.n and v < self.n:
            edge = tuple(sorted((u, v)))
            if edge not in self.connections:
                self.connections.append((edge))
            parU = self.find(u)
            parV = self.find(v)
            if parU != parV:
                self.parent[parU] = parV



    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]



    def remove(self, u, v):
        edge = tuple(sorted((u, v)))
        if u < self.n and v < self.n and edge in self.connections:
            self.connections.remove(edge)
            self.parent = []
            self.parent = [i for i in range(self.n)]

            for u, v in self.connections:
                self.add(u, v)




    def subgraphs(self):
        roots = set(self.find(i) for i in range(self.n))
        return len(roots)



if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 4), (2, 1),
             (2, 5), (3, 0),
             (5, 1))
    for u, v in edges:
        graph.add(u, v)

    print(graph.subgraphs())  # 2

    more_connections = ((0, 2), (2, 3),
                        (3, 5), (4, 5))
    for u, v in more_connections:
        graph.add(u, v)
    graph.remove(0,2)

    print(graph.subgraphs())  # 1