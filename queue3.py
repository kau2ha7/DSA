class Node:
    def __init__(self,item=None,next=None):
        self.item = item 
        self.next = next 


class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None
        self.count = 0
    def is_empty(self):
        return self.count == 0
    def enqueue(self,data):
        n = Node(item=data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.count +=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        else:
            if self.front == self.rear:
                self.front = None 
                self.rear = None 
            else:
                self.front = self.front.next 
            self.count -=1
    def get_front(self):
        if not self.is_empty():
            return self.front.item 
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item 
    def size(self):
        return self.count 
    
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front())
print(q1.get_rear())
print(q1.dequeue())
print(q1.get_front())  