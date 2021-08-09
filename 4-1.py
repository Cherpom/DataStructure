class queue():
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
        return ', '.join(str(data) for data in self.q) if self.size() != 0 else 'Empty'

input1 = input("Enter Input : ").split(",")
input1 = [i.split(" ") for i in input1]
Q1 = queue()
Q2 = queue()

for data in input1:
        if len(data) == 1:
            pop = Q1.dequeue()
            if pop != 'Empty':
                Q2.enqueue(pop)
                print(pop,'<-', end = ' ')
        else:
            Q1.enqueue(int(data[1]))
        print(Q1)

print(Q2, ':', Q1)