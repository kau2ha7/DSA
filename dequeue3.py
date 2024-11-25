class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item 
        self.next = next 
        self.prev = prev 

class Dequeue:
    def __init__(self):
        self.front=None 
        self.rear = None 
        self.count = 0
    def is_empty(self):
        return self.count == 0
    def insert_front(self,data):
        n = Node(item=data)
        if self.is_empty():
            self.rear = n
        else:
            n.next = self.front 
            self.front.prev = n
        self.front = n
        self.count +=1
    def insert_rear(self,data):
        n = Node(item=data)
        if self.is_empty():
            self.front = n
        else:
            n.prev = self.rear 
            self.rear.next = n
        self.rear = n
        self.count +=1
    def delete_front(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        else:
            if self.front == self.rear:
                self.front = None 
                self.rear = None 
            else:
                self.front = self.front.next 
                self.front.prev = None 
            self.count -=1
    def delete_rear(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        else:
            if self.front == self.rear:
                self.front = None 
                self.rear = None 
            else:
                self.rear = self.rear.prev 
                self.rear.next = None
            self.count -=1
    def get_front(self):
        if not self.is_empty():
            return self.front.item 
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item 
    def size(self):
        return self.count 
    

d1 = Dequeue()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front())
print(d1.get_rear())
d1.delete_front()
d1.delete_rear()
print(d1.get_front())
print(d1.get_rear())