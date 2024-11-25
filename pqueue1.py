class PQueue:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item) == 0
    def push(self,data,priority):
        index = 0
        while index < len(self.item) and self.item[index][1] <= priority:
            index +=1
        self.item.insert(index,(data,priority))
    def pop(self):
        if not self.is_empty():
            return self.item.pop(0)[0]
        else:
            raise IndexError('pqueue is empty')
    def size(self):
        return len(self.item)


p = PQueue()
p.push('kaushal', 1)
p.push('raj', 3)
p.push('karan', 5)

while not p.is_empty():
    print(p.pop())