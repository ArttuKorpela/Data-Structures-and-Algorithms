
class HashBucket:
    def __init__(self, M, B):
        if M % B != 0:
            raise ValueError("M should be divisible by B for equal sized buckets.")

        self.M = M
        self.B = B
        self.bucket_size = M // B
        self.table = [[None for _ in range(self.bucket_size)] for _ in range(B)]
        self.overflow = [None] * M

    def h(self, S):
        ascii_sum = sum(ord(char) for char in S)
        return ascii_sum % self.B

    def insert(self,data):
        if self.exists(data):
            return

        key = self.h(data)
        n = 0
        while n < self.bucket_size:
            if self.table[key][n] == None:
                self.table[key][n] = data
                return
            n += 1

        x = 0
        while x < self.M:
            if self.overflow[x] == None and self.overflow[x+1] == None:
                self.overflow[x] = data
                return
            x += 1

    def delete(self,data):
        key = self.h(data)
        n = 0

        while n < self.bucket_size:
            if self.table[key][n] == data:
                self.table[key][n] = None
                return
            n += 1

        for i in range(self.M):
            if self.overflow[i] == data:
                self.overflow[i] = None
                return

    def exists(self, data):
        key = self.h(data)
        if data in self.table[key]:
            return True
        if data in self.overflow:
            return True
        return False

    def print(self):
        final_string = " ".join(str(element) for row in self.table for element in row if element is not None)
        final_string = final_string + " " + " ".join([str(s) for s in self.overflow if s is not None])
        print(final_string)



if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()  # fOo BM40A1500 123 Bar1 10aaaa1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()  # BM40A1500 Bar1 10aaaa1
