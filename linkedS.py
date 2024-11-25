class Node:
    def __init__(self,item=None,next=None):
        self.item = item 
        self.next = next 

class Stack:
    def __init__(self):
        self.start = None 
        self.count = 0
    def is_empty(self):
        return self.start is None 
    def push(self,data):
        n = Node(data,self.start)
        self.start = n
        self.count +=1
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next 
            self.count -=1
            return data
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