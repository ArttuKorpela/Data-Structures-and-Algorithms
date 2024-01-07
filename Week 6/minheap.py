class MinHeap:
    def __init__(self, list):
            self.heap = list
            self.sortTheHeap()

    def sortTheHeap(self):
        for i in range(len(self.heap) // 2, -1, -1):
            self.sift_down(i)

    def push(self, key: int):
        self.heap.append(key)
        self.sift_up(len(self.heap) - 1)

    def pop(self):
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self.sift_down(0)
        return root

    def sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def sift_down(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.sift_down(smallest)

    def print(self):
        print(" ".join(map(str, self.heap)))

if __name__ == "__main__":
    heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
    heap.print()        # 1 4 2 5 8 6 3
    print(heap.pop())   # 1
    heap.push(9)
    heap.print()        # 2 4 3 5 8 6 9