class queue:
    def __init__(self,data):
        self.q = [i.split() for i in data]
    def enqueue(self,i):
        self.q.append(i)
    def dequeue(self):
        return self.q.pop(0) if self.size() != 0 else 'Empty'
    def isEmpty(self):
        return self.size() <= 0
    def size(self):
        return len(self.q)
    def __str__(self):
        return ', '.join(str(data) for data in self.q)

def convert_to_ord(char):
    return ord(char)
def convert_to_char(ord):
    return char(ord)

def encodemsg(q1,q2):
    display = list()
    cahce = int()
    plus = int()
    test = [int(i) for i in q2.q]
    for i in q1.q:
        asciicode = convert_to_ord(i)
        if(plus > q2.size()):
            plus = 0
        cahce = asciicode + q2.q[plus]
        plus = plus + 1
        display.append(covert_to_char(cahce))
    return display

input_string, input_number = input("Enter String and Code : ").split(',')
q_string = queue(input_string)
q_number = queue(input_number)
print(q_string)
print(q_number)
    
print(encodemsg(q_string,q_number))