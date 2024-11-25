class Node:
    def __init__(self, item=None, next=None, priority=None):
        self.item = item
        self.next = next
        self.priority = priority

class PQueue:
    def __init__(self):
        self.start = None
        self.count = 0

    def is_empty(self):
        return self.start is None

    def push(self, data, priority):
        n = Node(item=data, priority=priority)
        if self.is_empty() or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.count -= 1
            return data
        else:
            raise IndexError('pqueue is empty')

    def size(self):
        return self.count

# Test
p = PQueue()
p.push('kaushal', 1)
p.push('raj', 3)
p.push('karan', 5)

while not p.is_empty():
    print(p.pop())
