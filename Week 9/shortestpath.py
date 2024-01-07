import math

class Graph:
    def __init__(self, n):
        self.n = n
        #Itse lista yhteyksistä
        self.graph_list = [[] for _ in range(n)]
        #Lista jos on käyty, alustetaan.
        self.visited = [False] * n
        #Etäisyydet lähtöpisteestä
        self.paths = [math.inf] * n
        #Edeltäneet vertex:it
        self.predecessors = [-1] * n

    def add(self, u, v, w):
        self.graph_list[u].append((v, w))

    def remove(self, u, v):
        for index, edge in enumerate(self.graph_list[u]):
            if edge[0] == v:
                self.graph_list[u].pop(index)
                break

    def shortest_path(self, start, end):
        #Alustus
        self.visited = [False] * self.n
        self.paths = [math.inf] * self.n
        self.paths[start] = 0
        self.predecessors = [-1] * self.n


        for i in range(self.n):
            #Etsitään pienin vertex, jossa ei ole käyty
            v = self.min_vertex()
            #Merkitään tämä käydyksi
            self.visited[v] = True
            #Tarkistetaan, että on mahdollista päästä
            if self.paths[v] == math.inf:
                break
            #Vertex:in edget ja niiden painot
            for neighbor, weight in self.graph_list[v]:
                if not self.visited[neighbor]:
                    new_distance = self.paths[v] + weight
                    if new_distance < self.paths[neighbor]:
                        #Lisätään uusi etäisyys, jos etäisyys on pienempi, kuin edellinen
                        self.paths[neighbor] = new_distance
                        #Lisätään edeltäjä listaan v:n kohdalle
                        self.predecessors[neighbor] = v  # Update predecessor

        print(*self.get_path(end))

    def get_path(self, end):
        path = []
        #Alustetaan nykyinen tavoitelemallamme vertx:illä
        current = end
        while current != -1:#Toistamme kunnes osumme -1, joka merkkaa ettei tällä vertex:illä ole edeltäjiä
            path.insert(0, current)#Sijoitetaan nykyinen polun alkuun
            current = self.predecessors[current]#Otetaan edejtäjien listasta nykyisen edelltäjä
        if len(path) == 1:
            path = [-1]
        return path

    def min_vertex(self):
        min_value = math.inf
        min_vertex = -1
        for i in range(self.n):
            #käydään läpi lista etäisyyksistä, etsitään pienin vertix
            #jossa ei olla käyty
            if not self.visited[i] and self.paths[i] < min_value:
                min_value = self.paths[i]
                min_vertex = i
        return min_vertex



if __name__ == "__main__":

    graph = Graph(10)
    edges = ((0, 1, 25), (0, 2,  6), (1, 3, 10),
             (1, 4,  3), (2, 3,  7), (2, 5, 25),
             (3, 4, 12), (3, 5, 15), (3, 6,  4),
             (3, 7, 15), (3, 8, 20), (4, 7,  2),
             (5, 8,  2), (6, 7,  8), (6, 8, 13),
             (6, 9, 15), (7, 9,  5), (8, 9,  1))
    for u, v, w in edges:
        graph.add(u, v, w)

    graph.shortest_path(0, 9)   # 0 2 3 6 7 9
    graph.remove(3, 6)
    graph.remove(5, 6)
    graph.shortest_path(0, 9)   # 0 2 3 5 8 9