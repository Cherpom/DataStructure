class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return self.data

class Queue:
    def __init__(self):
        self.lst = list()
    def enqueue(self,data):
        self.lst.append(data)
    def dequeue(self,data):
        self.lst.remove(data)
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return self.lst == 0

class BST:
    def __init__(self):
        self.root = None
    def insert(self,data):
        ## Empty tree
        if self.root is None:
            self.root = data
            return
        node = self.root
        while True:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                    return self.root
                node = node.left
                elif node.right == None:
                    node.right = Node(data)
                    return self.root
            else:
                if node.left == None:
                    node.left = Node(data)
                    return self.root
                elif node.right == None:
                    node.right = Node(data)
                    return self.root

        def printTree(self, node, level = 0):
            if node != None:
                self.printTree(node.right, level + 1)
                print('     ' * level, node)
                self.printTree(node.left, level + 1)
'''
     5
    / \
   3   7
  / \
 2   4          input = 6

 less_than(root,6) -> node(5)
>> n = self.less_than(node(3),6)
    >> n = self.less_than(node(2),6)
        >> n = self.less_than(node(leftNone),6)         now node(2)
            >> n = return 0                             now node(leftNone) goto node(2)
        >> if 2 > 6 (false)         n = 0               now node(2)
        >> n += self.less_than(node(rightNone),6)
            >> n = return 0         n = 0 + 0           now node(rightNone) goto node(2)
        >> if 2 <= 6 (True)         n = 0 + 0 + 1
        >> return n                 n = 1               now node(2) goto node(3)
    >> if 3 > 6 (false)         n(3) = 1
    >> n += self.less_than(node(4),6)     n(3) = 1         now node(3) goto node(4)
        >> n = self.less_than(node(leftNone),6)         now node(4) goto leftNone
            >> n = return 0         n(4) = 0               now node(leftNone) goto node(4)
        if 4 > 6 (false)            n(4) = 0
        >> n += self.less_than(node(rightNone),6)        now node(4) goto rightNone
            >> n = return 0         n = 0               now node(rightNone) goto node(4)
        >> if 4 <= 6 (True)         n = 0 + 0


'''
        def less_than(self,node,data):
            if node == None:
                return 0
            n = self.less_than(node.left,data)
            if node.data > data:
                return n
            n += self.less_than(node.right,data)

            if node.data <= data:
                n += 1
            return n