

class HashLinear:
    def __init__(self, M):
        self.M = M
        self.list = [None] * self.M
        self.current = 0

    def h(self,S):
        ascii_sum = sum(ord(char) for char in S)
        return ascii_sum % self.M

    def insert(self,data):
        key = self.h(data)
        n = 0

        if self.current >= self.M:
            return

        while self.list[key] != None and n < self.M:
            key = (key + 1) % self.M
            n += 1
        if self.list[key] == None:
            self.list[key] = data
            self.current += 1

    def delete(self, data):
        key = self.h(data)
        n = 0
        while self.list[key] != data and n < self.M:
            key = (key + 1) % self.M
            n += 1

        if self.list[key] == data:
            self.list[key] = None
            self.current -= 1

    def print(self):
        final_string = " ".join([s for s in self.list if s is not None])
        print(final_string)

if __name__ == "__main__":
    table = HashLinear(10)
    table.insert("buttermilk")
    table.insert("shim")
    table.insert("resolvend")
    table.insert("cheiromegaly")
    table.insert("premillennialise")
    table.insert("finebent")
    table.print()
    table.delete("buttermilk")
    table.delete("cores")
    table.delete("cheiromegaly")
    table.delete("iodations")
    table.print()
    table.insert("iodations")
    table.insert("tirrlie")
    table.insert("comous")
    table.insert("discursiveness")
    table.insert("flabbergasts")
    table.insert("rename")
    table.insert("softhead")
    table.print()
