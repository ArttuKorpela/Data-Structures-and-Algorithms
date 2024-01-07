class Node:

    def __init__(self,data,next):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.len = 0

    def append(self, data):
        newNode = Node(data, None)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.len += 1

    def insert(self,data,i):
        newNode = Node(data,None)
        cur = self.head

        if self.len < i-1:
            return
        if i == 0:
            cur = self.head
            newNode.next = cur
            self.head = newNode
            self.len += 1
            return

        else:
            for j in range(i-1):
                cur = cur.next

        temp = cur.next
        newNode.next = temp
        cur.next = newNode
        self.len += 1

    def delete(self, index):
        if index < 0 or index >= self.len:

            return None

        current = self.head
        if index == 0:
            removed_data = current.data
            self.head = current.next
            if self.head is None:
                self.tail = None
        else:
            for _ in range(index - 1):
                current = current.next
            removed_data = current.next.data
            current.next = current.next.next
            if current.next is None:
                self.tail = current

        self.len -= 1
        return removed_data


    def __str__(self):

        temp = self.head
        elements = []
        while temp != None:
            elements.append(str(temp.data))
            temp = temp.next
        return " -> ".join(elements)

    def print(self):
        print(self)

    def index(self,data):
        n = 0
        temp = self.head

        while temp is not None:
            if data == temp.data:
                return n
            else:
                temp = temp.next
            n += 1

        return -1

    def getData(self, i):
        if i >= self.len or i < 0:
            return None
        cur = self.head
        for _ in range(i):
            cur = cur.next
        return cur.data

    def setData(self, i, data):
        if i >= self.len or i < 0:
            return
        cur = self.head
        for _ in range(i):
            cur = cur.next
        cur.data = data

    def swap(self, i, j):
        if i >= self.len or j >= self.len or i < 0 or j < 0:
            return
        iD = self.getData(i)
        jD = self.getData(j)

        self.setData(i, jD)
        self.setData(j, iD)








if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.print()  # 1 -> 3
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()  # 15 -> 1 -> 10 -> 3
    print(L.index(10))
    L.swap(0,3)
    L.print()  # 1 -> 10 -> 3