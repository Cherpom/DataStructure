class Queue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        return ', '.join(str(data) for data in self.queue) if self.size() != 0 else 'Empty'

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        return self.queue.pop(0) if self.size() != 0 else 'Empty'

    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    money = 15000
    for i in range(0,30):
        money = money + money/100;
    print(money)