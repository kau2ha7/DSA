class Dequeue(list):
    def is_empty(self):
        return len(self) == 0
    def insert_front(self,data):
        self.insert(0,data)
    def insert_rear(self,data):
        self.append(data)
    def delete_front(self):
        if not self.is_empty():
            return super().pop(0)
        else:
            raise IndexError('deque is empty')
    def delete_rear(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError('deque is empty')
    def get_front(self):
        if not self.is_empty():
            return self[0]
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
    def size(self):
        return len(self)
    

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