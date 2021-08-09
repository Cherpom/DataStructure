class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if node.data < data:
                if node.right is None:
                    node.right = Node(data)
                    return self.root
                node = node.right
            elif node.data > data:
                if node.left is None:
                    node.left = Node(data)
                    return self.root
                node = node.left
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def findMax(self):
        if self.root is None:
            return
        else:
            temp = int()
            node = self.root
            while True:
                if node.right is None:
                    return node.data
                node = node.right
    
    def findMin(self):
        if self.root is None:
            return
        else:
            temp = int()
            node = self.root
            while True:
                if node.left is None:
                    return node.data
                node = node.left

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print("Min :", T.findMin())
print("Max :", T.findMax())