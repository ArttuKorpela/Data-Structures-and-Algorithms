import math


class Graph:

    def __init__(self, n):
        self.n = n
        self.graph_matrix = [[math.inf] * n for i in range(n)]


    def add(self, u, v, w):
        if u >= self.n or v >= self.n:
            pass
        else:
            self.graph_matrix[u][v] = w



    def remove(self, u, v):
        self.graph_matrix[u][v] = math.inf

    def all_paths(self):
        D = [[-1] * self.n for i in range(self.n)]

        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    D[i][j] = 0
                else:
                    D[i][j] = self.graph_matrix[i][j]
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if (D[i][k] != -1 and
                        D[k][j] != -1 and
                        D[i][j] > D[i][k] + D[k][j]):
                            D[i][j] = D[i][k] + D[k][j]
        for i in range(self.n):
            for j in range(self.n):
                if D[i][j] == math.inf:
                    D[i][j] = -1

        return D


if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
             (2, 3, 1), (2, 5, 2), (3, 0, 6),
             (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    M = graph.all_paths()
    for weights in M:
        for weight in weights:
            print(f"{weight:3d}", end="")
        print()
    #  0 12  7  8  9  9
    # -1  0 -1 -1 -1 -1
    #  7  5  0  1 16  2
    #  6  8 13  0 15  2
    # -1  7 -1 -1  0  1
    # -1  6 -1 -1 -1  0