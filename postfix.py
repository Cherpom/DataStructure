class Stack:
    def __init__(self):
        self.stackList = list()
    def push(self,data):
        self.stackList.append(data)
    def peek(self):
        if self.is_empty:
            return "List is Empty"
        return self.stackList[-1]
    def is_empty(self):
        return self.stackList == []
    def pop(self):
        if self.is_empty:
            return "List is Empty"
        return self.stackList.pop()

def infix_to_postfix(inlist):
    priority = {'(': -5, '+': 0, '-': 0, '*': 2, '/': 2}
    return_string = ''
    s = Stack()
    for i in inlist:
        if i in '+-*/':
            if s.is_empty():
                s.push(i)
            else:
                print("in this if")
                print(i)
                while not s.is_empty():
                    if s.peek() == '(':
                        break
                    else:
                        if priority.get(s.peek(),-2) < priority.get(i,-2):
                            break
                        else:
                            return_string += str(s.pop())
                    s.push(i)
        elif i == '(':
            s.push(i)
        elif i == ')':
            while s.peek() != '(':
                return_string =+ str(s.pop())
            s.pop()
        else: #Character
            return_string += i
    while not s.is_empty:
        return_string += str(s.pop())
    return return_string

lst = ['a', '+', 'b', '*', 'c']
print(infix_to_postfix(lst))