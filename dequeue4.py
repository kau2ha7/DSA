from dlink import *

class Dequeue:
    def __init__(self):
        self.item = DLL()
        self.count = 0
    def is_empty(self):
        return self.item.is_empty()
    def insert_front(self,data):
        self.item.insert_first(data)
        self.count +=1
    def insert_rear(self,data):
        self.item.insert_last(data)
        self.count +=1
    def delete_front(self):
        if not self.is_empty():
            self.count -=1
            return self.item.delete_first()
        else:
            raise IndexError('deque is empty')
    def delete_rear(self):
        if not self.is_empty():
            self.count -=1
            return self.item.delete_last()
        else:
            raise IndexError('deque is empty')
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
