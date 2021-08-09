class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, table_size, max_collisions):
        self.table_size = table_size
        self.max_collisions = max_collisions
        self.table = list()
        for i in range(table_size):
            self.table.append(None)
    def get_hashcode(self,key):
        index = int(0)
        for character in key:
            index += ord(character)
        return index % self.table_size
    def isFull(self):
        check = int(0)
        for i in self.table:
            if i is not None:
                check += 1
        return check is self.table_size
    def insert(self, data):
        if self.isFull():
            print("This table is full !!!!!!")
            quit()
        key, value = data.key, data.value
        collision_count = 0
        hashIndex = self.get_hashcode(key)
        while collision_count < self.max_collisions:
            index = (hashIndex + collision_count ** 2) % table_size
            if self.table[index] == None:
                self.table[index] = data
                return
            collision_count += 1
            print(f'collision number {collision_count} at {index}')
        print("Max of collisionChain")
    def __str__(self):
        out = ''
        for i in range(self.table_size):
            out += f"#{i+1}\t{self.table[i]}\n"
        out += '---------------------------'
        return out
    
if __name__ == '__main__':
    print(" ***** Fun with hashing *****")
    control, lst = input("Enter Input : ").split('/')
    table_size, max_collision = list(map(int, control.split()))
    lst = lst.split(',')
    data_lst = []
    for item in lst:
        key, value = item.split()
        data_lst.append(Data(key, value))

    hash = Hash(table_size, max_collision)
    for data in data_lst:
        hash.insert(data)
        print(hash)