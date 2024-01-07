import copy
import math


class Graph:

    def __init__(self, n):
        self.n = n;
        self.graph_matrix = [[0] * n for i in range(n)]
        self.ans = [];

    def add(self,from_u, to_v):
        self.graph_matrix[from_u][to_v] = 1
        self.graph_matrix[to_v][from_u] = 1

    def remove(self, from_u, to_v):
        self.graph_matrix[from_u][ to_v] = 0
        self.graph_matrix[to_v][from_u] = 0

    def dft(self, start):
        visited = [False] * self.n
        self.ans = []
        self.dft_help_3(start, visited)
        print(*self.ans)

    def bft(self, start):
        self.ans = []
        visited = [False] * self.n
        queue = [start]
        while queue:
            c = queue.pop(0)
            if not visited[c]:
                visited[c] = True
                self.ans.append(c)
                for i in range(self.n):
                    if self.graph_matrix[c][i] == 1 and not visited[i]:
                        queue.append(i)
        print(*self.ans)



    def old_bft(self,start):
        self.ans = [start]
        cp_graph = copy.deepcopy(self.graph_matrix)
        self.bft_help_2(start,cp_graph)
        print(*self.ans)

    def bft_help_2(self,c,g):
        row1 = g[c]
        row2 = []
        for i in range(self.n):
            row2.append(g[i][c])
        temp = list()

        for index, (item1, item2) in enumerate(zip(row1, row2)):
            if item1 == 1 or item2 == 1:
                temp.append(index)
        if temp == []:
            return
        else:
            temp.sort()
            print(temp)
            for i in temp:
                if i not in self.ans:
                    self.ans.append(i)
                    g[i][c] = 0
                    g[c][i] = 0

            for i in temp:
                if i in self.ans:
                    continue
                else:
                    self.bft_help_2(i,g)


    def dft_help(self,c,g):
        n = 0

        for item in g[c]:
            if item == 1 and n not in self.ans:
                g[c][n] = 0
                self.ans.append(n)
                self.dft_help(n,g)

            else:
                n+=1
        for item in range(n):
            if g[item][c] == 1 and item not in self.ans:
                g[item][c]=0
                self.ans.append(item)
                self.dft_help(item,g)

        return

    def dft_help_2(self,c,g):
        row1 = g[c]
        row2 = []
        for i in range(self.n):
            row2.append(g[i][c])

        index = self.find_first_one(row1,row2)
        if index is None:
            if c == self.n-1 or c == 0:
                return
            else:
                self.dft_help_2(c-1,g)
        else:
            self.ans.append(index)
            g[index][c] = 0
            g[c][index] = 0
            self.dft_help_2(index, g)



    def dft_help_3(self, c, visited):
        visited[c] = True
        self.ans.append(c)
        for i in range(self.n):
            if self.graph_matrix[c][i] == 1 and not visited[i]:
                self.dft_help_3(i, visited)





    def find_first_one(self,list1, list2):
        for index, (item1, item2) in enumerate(zip(list1, list2)):
            if item1 == 1 or item2 == 1:
                if index not in self.ans:
                    return index
        return None



if __name__ == "__main__":
    graph = Graph(8)

    connections = ((0, 6), (0, 7), (1, 0),
                   (1, 2), (2, 3), (3, 6),
                   (4, 3), (5, 4), (5, 6),
                   (6, 1), (6, 2), (6, 7))

    for u, v, in connections:
        graph.add(u, v)

    graph.dft(0)
    graph.bft(7)

    graph.remove(7, 0)
    graph.remove(5, 4)
    graph.remove(2, 1)

    graph.dft(0)
    graph.bft(7)