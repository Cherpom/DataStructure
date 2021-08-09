class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.front = None
        self.listSize = 0
    def __str__(self):
        if(self.isEmpty()):
            return ""
        display = str()
        count = int(0)
        node = self.front
        display += node.data
        while(node.next != None):
            node = node.next
            display = display + "->"
            display += node.data
        return display
    def isEmpty(self):
        return self.front == None
    def append(self,data):
        self.listSize += 1
        if(self.isEmpty()):
            self.front = Node(data)
            return
        node = self.front
        while(node.next != None):
            node = node.next
        node.next = Node(data)
        return
    def size(self):
        return self.listSize
    def addFront(self,data):
        self.listSize += 1
        if(self.front == None):
            self.front = Node(data)
            return
        node = self.front
        temp = node.next
        self.front = Node(data)
        self.front.next = node
    def isInList(self,data):
        if(self.front == None):
            return False
        node = self.front
        while(node.next != None):
            if(node.data == data):
                return True
            node = node.next
        if(node.data == data):
            return True
        return False
    def insert(self,index,data):
        self.listSize += 1
        if(self.isEmpty()):
            self.front = Node(data)
            return
        node = self.front
        if(index == 0):
            self.addFront(data)
            return
        for i in range(index-1):
            node = node.next
        temp = node.next
        node.next = Node(data)
        node = node.next
        node.next = temp
    
input1 = input("Enter Input : ").split(",")
inLinkListed, changeLinkList = input1[0].split(), [input1[i].split(":") for i in range(1,len(input1))]
L = LinkedList()
for i in inLinkListed:
    L.append(i)
if(L.size() == 0):
    print("List is empty")
else:
    print("link list : " + str(L))
for i in range(len(changeLinkList)):
    if(int(changeLinkList[i][0]) >= 0 and int(changeLinkList[i][0]) <= L.size()):
        print("index = " + str(int(changeLinkList[i][0])) + " and data = " + changeLinkList[i][1])
        L.insert(int(changeLinkList[i][0]), changeLinkList[i][1])
    else:
        print("Data cannot be added")
    if(L.size() == 0):
        print("List is empty")
    else:
        print("link list : " + str(L))