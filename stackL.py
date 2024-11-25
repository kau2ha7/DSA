class Stack:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item) == 0
    def push(self,data):
        self.item.append(data)
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError('stack is empty')
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
    def size(self):
        return len(self.item)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.size())  