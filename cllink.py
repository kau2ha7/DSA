class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last=None):
        self.last = last
    
    def is_empty(self):
        return self.last is None
    
    def insert_first(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    def search(self, data):
        if not self.is_empty():
            temp = self.last.next
            while True:
                if temp.item == data:
                    return temp
                temp = temp.next
                if temp == self.last.next:
                    break
        return None

    def insert_after(self, temp, data):
        n = Node(data, temp.next)
        temp.next = n
        if temp == self.last:
            self.last = n

    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while True:
                print(temp.item, end=' ')
                temp = temp.next
                if temp == self.last.next:
                    break
            print()

    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_item(self, data):
        if not self.is_empty():
            if self.last.next == self.last and self.last.item == data:
                self.last = None
            elif self.last.next.item == data:
                self.delete_first()
            else:
                temp = self.last.next
                while temp.next != self.last:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        return
                    temp = temp.next
                if self.last.item == data:
                    self.delete_last()

    def __iter__(self):
        if self.last is None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)
        
class CLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start 
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None or (self.current == self.start and self.count == 1):
            raise StopIteration
        if self.current == self.start:
            self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data

# Example usage:
cll = CLL()
cll.insert_last(1)
cll.insert_last(2)
cll.insert_last(3)
cll.insert_first(0)
cll.print_list()  # Output: 0 1 2 3
cll.delete_item(2)
cll.print_list()  # Output: 0 1 3
for item in cll:
    print(item, end=' ')  # Output: 0 1 3
print()
