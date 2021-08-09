class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.listsize = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        self.listsize += 1
        if(self.head == None):
            self.head = Node(item)
            self.tail = self.head
            return
        node = self.head
        temp = node
        while(node.next != None):
            node = node.next
            temp = node
        node.next = Node(item)
        node.next.previous = temp
        self.tail = node.next

    def addHead(self, item):
        self.listsize += 1
        if(self.isEmpty()):
            self.head = Node(item)
            self.tail = self.head
            return
        node = self.head
        self.head = Node(item)
        temp = self.head
        self.head.next = node
        self.head.next.previous = temp

    def insert(self, pos, item):
        if(self.head == None):
            self.listsize += 1
            self.head = Node(item)
            self.tail = self.head
            return
        if(pos == 0):
            self.addHead(item)
            return
        node = self.head
        if(pos < 0):
            pos = self.listsize + pos - 1
        if(pos < 0):
            self.addHead(item)
        elif(pos >= self.listsize):
            self.append(item)
        elif(pos >= 0 and pos < self.listsize):
            self.listsize += 1
            for i in range(pos):
                node = node.next
            temp_next = node.next
            node.next = Node(item)
            temp_previous = node
            node = node.next
            node.previous = temp_previous
            node.next = temp_next
            node.next.previous = node

    def search(self, item):
        node = self.head
        if(node.value == item):
            return str("Found")
        for i in range(self.listsize-1):
            node = node.next
            if(node.value == item):
                return str("Found")
        return str("Not Found")

    def index(self, item):
        node = self.head
        if(self.listsize == 1 and node.value == item):
            return 0
        for i in range(self.listsize-1):
            if(node.value == item):
                return i
            node = node.next
        return -1

    def size(self):
        return self.listsize

    def pop(self, pos):
        node = self.head
        if(-(self.listsize) <= pos and pos < self.listsize):
            if(pos < 0):
                pos = self.listsize + pos
            for i in range(pos-1):
                node = node.next
            if(pos == 0 and self.listsize == 1):
                node.next = None
                self.tail = None
                self.head = None
            elif(pos == 0):
                node.next.previous = None
                self.head = node.next
            else:
                temp1 = node
                node = node.next
                temp2 = node.next
                node = node.next
                node.previous = temp1
                node.previous.previous.next = temp2
            self.listsize -= 1    
            return str("Success")
        else:
            return str("Out of Range")

input1 = input("Enter Input (L1,L2) : ").split()
input1 = [i.split("->") for i in input1]
L1 = LinkedList()
L2 = LinkedList()
for i in input1[0]:
    L1.append(i)
for i in input1[1]:
    L2.append(i)
print("L1    : ",end='')
print(L1)
print("L2    : ",end='')
print(L2)
'''L1.tail.next = L2.head
L1.tail.next.previous = L1.tail'''
print("Merge : ",end='')
print(L1,end='')
print(L2.reverse(),end='')
