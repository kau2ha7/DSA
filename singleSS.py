from slink import *

class Stack(SLlist):
    def __init__(self, start=None):
        super().__init__(start)
        self.count = 0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_start(data)
        self.count +=1
    def pop(self):
        if not self.is_empty():
            self.count -=1
            return self.delete_first()
        else:
            raise IndexError('stack is empty')
    def peek(self):
        if not self.is_empty():
            return self.start.item 
    def size(self):
        return self.count 
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.size())  