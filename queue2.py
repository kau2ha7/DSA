class Queue(list):
    def is_empty(self):
        return len(self) == 0
    def enqueue(self,data):
        self.append(data)
    def dequeue(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError('queue is empty')
    def get_front(self):
        if not self.is_empty():
            return self[0]
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
    def size(self):
        return len(self)

q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front())
print(q1.get_rear())
print(q1.dequeue())
print(q1.get_front())  