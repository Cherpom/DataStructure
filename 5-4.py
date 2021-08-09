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
            return ""
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
                self.listsize -= 1
                return node.value
            elif(pos == 0):
                node.next.previous = None
                return_value = node.value
                self.head = node.next
                self.listsize -= 1
                return return_value
            elif(pos == self.listsize-1):
                return_value = node.next.value
                node.next = None
                self.listsize -= 1
                return return_value
            else:
                temp1 = node
                node = node.next
                return_value = node.value
                temp2 = node.next
                node = node.next
                node.previous = temp1
                node.previous.previous.next = temp2
                self.listsize -= 1
                return return_value
        else:
            return str("Out of Range")

input1 = input("Enter Input : ").split(",")
List_Left = LinkedList()
List_Right = LinkedList()
for i in input1:
    if i[:1] == "I":
        List_Left.append(i[2:])
    elif i[:1] == "L":
        if(List_Left.size() != 0):
            List_Right.addHead(List_Left.pop(List_Left.size() - 1))
    elif i[:1] == "R":
        if(List_Right.size() != 0):
            List_Left.append(List_Right.pop(0))
    elif i[:1] == "B":
        if(List_Left.size() != 0):
            List_Left.pop(List_Left.size()-1)
    elif i[:1] == "D":
        if(List_Right.size() != 0):
            List_Right.pop(0)
#print format
print(f'{List_Left}| {List_Right}')