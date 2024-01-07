class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None
        self.is_mirrored = False

    def insert(self, key):
        if self.root and ((self.root.left and self.root.left.key > self.root.key) or
                          (self.root.right and self.root.right.key < self.root.key)):
            self.mirror()
            self.root = self._insert_recursive(self.root, key)
            self.mirror()
        else:
            self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)

        if self.is_mirrored:
            if key > node.key:
                node.left = self._insert_recursive(node.left, key)
            else:
                node.right = self._insert_recursive(node.right, key)
        else:
            if key < node.key:
                node.left = self._insert_recursive(node.left, key)
            else:
                node.right = self._insert_recursive(node.right, key)

        return node


    def preorder(self):
        self.preorder_rec(self.root)
        print()

    def preorder_rec(self, node):

        if node:
            print(node.key, end=" ")

            self.preorder_rec(node.left)
            self.preorder_rec(node.right)

    def search(self, key):
        if self.root and ((self.root.left and self.root.left.key > self.root.key) or
                          (self.root.right and self.root.right.key < self.root.key)):
            self.mirror()
            ans = self.search_rec(self.root, key)
            self.mirror()
        else:
            ans = self.search_rec(self.root, key)

        return ans

    def search_rec(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True

        if self.is_mirrored:
            if key > node.key:
                return self.search_rec(node.left, key)
            else:
                return self.search_rec(node.right, key)
        else:
            if key < node.key:
                return self.search_rec(node.left, key)
            else:
                return self.search_rec(node.right, key)

    def getmax(self, node):
        if node.right == None:
            return node.key
        else:
            return self.getmax(node.right)

    def remmax(self, node):
        if node.right == None:
            return node.left
        node.right = self.remmax(node.right)
        return node

    def remove(self, key):
        if self.root and ((self.root.left and self.root.left.key > self.root.key) or
                          (self.root.right and self.root.right.key < self.root.key)):
            self.mirror()
            self.root = self.remove_rec(self.root, key)
            self.mirror()
        else:
            self.root = self.remove_rec(self.root, key)

    def remove_rec(self, node, key):
        if node == None:
            return None

        if self.is_mirrored:
            if key > node.key:
                node.left = self.remove_rec(node.left, key)
            else:
                node.right = self.remove_rec(node.right, key)
        else:
            if key < node.key:
                node.left = self.remove_rec(node.left, key)
            elif key > node.key:
                node.right = self.remove_rec(node.right, key)

        if node.key == key:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                if self.is_mirrored:
                    node.key = self.getmin(node.right)
                    node.right = self.remmin(node.right)
                else:
                    node.key = self.getmax(node.left)
                    node.left = self.remmax(node.left)

        return node

    def postorder(self):
        self.postorder_rec(self.root)
        print()

    def postorder_rec(self, node):
        if node:
            self.postorder_rec(node.left)
            self.postorder_rec(node.right)
            print(node.key, end=" ")

    def inorder(self):
        self.inorder_rec(self.root)
        print()

    def inorder_rec(self, node):
        if node:
            self.inorder_rec(node.left)
            print(node.key, end=" ")
            self.inorder_rec(node.right)

    def breadthfirst(self):
        root = self.root
        list = []

        if root is None:
            return

        list.append(root)
        while (len(list) > 0):
            print(list[0].key, end=" ")
            node = list.pop(0)

            if node.left != None:
                list.append(node.left)
            if node.right != None:
                list.append(node.right)

    def mirror(self):
        self.root = self.mirror_rec(self.root)
        self.is_mirrored = not self.is_mirrored


    def mirror_rec(self, node):
        if node is None:
            return None

        if node.left is not None or node.right is not None:
            node.left, node.right = node.right, node.left

        self.mirror_rec(node.left)
        self.mirror_rec(node.right)

        return node





if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()  # 5 1 3 2 4 9 7 6
    Tree.mirror()
    Tree.preorder()  # 5 9 7 6 1 3 4 2

    Tree.insert(8)
    Tree.remove(3)
    print(Tree.search(2))  # True
    Tree.preorder()  # 5 9 7 8 6 1 2 4
    Tree.mirror()
    Tree.preorder()  # 5 1 2 4 9 7 6 8

