class Stack(list):
    def is_empty(self):
        return len(self) == 0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError('stack is empty')
    def peek(self):
        if not self.is_empty():
            return self[-1]
    def size(self):
        return len(self)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.size())  