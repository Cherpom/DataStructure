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

    def lessThan(self, node, data):
        if node == None:
            return 0
        count = self.lessThan(node.left, data)
        if node.data > data:
            return count
        count += self.lessThan(node.right, data)
        if node.data <= data:
            count += 1
        return count

T = BST()
inp = input('Enter Input : ').split("/")
numList = [int(i) for i in inp[0].split()]
for i in numList:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(T.lessThan(root,int(inp[1])))