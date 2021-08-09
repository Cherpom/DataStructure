class queue:
    def __init__(self):
        self.q = list()
    def enqueue(self,i):
        self.q.append(i)
    def dequeue(self):
        return self.q.pop(0) if self.size() != 0 else 'Empty'
    def isEmpty(self):
        return self.size() <= 0
    def size(self):
        return len(self.q)
    def __str__(self):
        return q[0] if self.size() != 0 else 'Empty'

lst = [data.split() for data in input("Enter Input : ").split(",")]
normalQueue = queue()
specialQueue = queue()

for data in lst:
    if(len(data) == 1):
        if(specialQueue.isEmpty()):
            print(normalQueue.dequeue())
        else:
            print(specialQueue.dequeue())
    else:
        if(data[0] == "EN"):
            normalQueue.enqueue(data[1])
        elif(data[0] == "ES"):
            specialQueue.enqueue(data[1])