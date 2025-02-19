class Queue:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item) == 0
    def enqueue(self,data):
        self.item.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            raise IndexError('queue is empty')
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
    def size(self):
        raise len(self.item)

q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front())
print(q1.get_rear())
print(q1.dequeue())
print(q1.get_front())  