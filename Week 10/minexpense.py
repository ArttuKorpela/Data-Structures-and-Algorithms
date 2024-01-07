import math


class Graph:

    def __init__(self, n):
        self.n = n
        self.graph_matrix = [[math.inf] * n for i in range(n)]
        self.parent = [i for i in range(self.n)]
        self.visited_edges = list()
        self.visited_nodes = set()


    def add(self, u, v, w):
        if u >= self.n or v >= self.n:
            pass
        elif self.graph_matrix[u][v] != math.inf:
            if self.graph_matrix[u][v] < w:
                pass
        elif self.graph_matrix[v][u] != math.inf:
            if self.graph_matrix[v][u] < w:
                pass

        else:
            self.graph_matrix[u][v] = w
            self.graph_matrix[v][u] = w

            #self.union(u,v)



    def remove(self, u, v):
        self.graph_matrix[u][v] = math.inf

    def min(self):
        min_weight = math.inf
        for i in range(self.n):
            for j in range(self.n):
                if self.graph_matrix[i][j] < min_weight and (i, j) not in self.visited_edges:
                    if self.find(i) != self.find(j):
                        min_weight = self.graph_matrix[i][j]
                        min_i = i
                        min_j = j
        self.visited_edges.append((min_i, min_j))
        self.visited_edges.append((min_j, min_i))
        self.visited_nodes.add(min_i)
        self.visited_nodes.add(min_j)
        self.union(min_i,min_j)
        return min_weight





    def min_expense(self):
        self.parent = [i for i in range(self.n)]
        self.visited_edges = list()
        self.visited_nodes = set()
        total = 0
        while True:
            if len(self.visited_nodes) == self.n:
                return total
            else:
                total += self.min()
                print(self.visited_nodes)



    def union(self,u,v):
        parU = self.find(u)
        parV = self.find(v)
        if parU != parV:
            self.parent[parU] = parV


    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

if __name__ == "__main__":
    graph = Graph(6)
    edges = ((1, 2, 17), (4, 6, 14), (2, 5, 15),
                   (3, 4, 3), (0, 5, 18), (3, 5, 8),
                   (2, 0, 9), (0, 2, 19), (0, 1, 10),
                   (1, 0, 13), (4, 1, 12), (5, 1, 3))
    for u, v, w in edges:
        graph.add(u, v, w)

    print(graph.min_expense())  # 15

    graph.remove(2, 3)

    print(graph.min_expense())  # 16