from slink import *

class Queue:
    def __init__(self):
        self.item = SLlist()
        self.count = 0
    def is_empty(self):
        return self.item.is_empty()
    def enqueue(self,data):
        self.item.insert_start(data)
        self.count +=1
    def dequeue(self):
        if not self.is_empty():
            self.count -=1
            return self.item.delete_first()
        else:
            raise IndexError('queue is empty')
    def get_front(self):
        if not self.is_empty():
            return self.item.start.item 
    def get_rear(self):
        if not self.is_empty():
            temp = self.item.start 
            while temp.next is not None:
                temp = temp.next 
            return temp.item 
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