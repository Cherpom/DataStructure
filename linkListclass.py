class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.listSize = 0
    def size(self):
        return self.listSize
    def isEmpty(self):
        return self.listSize == 0
    def index_value(self,index):
        pass
    def index(self,data):
        pass
    