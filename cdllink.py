class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next 

class CDLL:
    def __init__(self, start=None):
        self.start = start 

    def is_empty(self):
        return self.start is None

    def insert_first(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
            self.start = n

    def insert_last(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n

    def search(self, data):
        if not self.is_empty():
            temp = self.start
            while True:
                if temp.item == data:
                    return temp
                temp = temp.next 
                if temp == self.start:
                    break
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(prev=temp, item=data, next=temp.next)
            temp.next.prev = n
            temp.next = n

    def print_list(self):
        if not self.is_empty():
            temp = self.start
            while True:
                print(temp.item, end=' ')
                temp = temp.next 
                if temp == self.start:
                    break
            print()

    def delete_first(self):
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.next.prev = self.start.prev 
                self.start.prev.next = self.start.next 
                self.start = self.start.next 

    def delete_last(self):
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev

    def delete_item(self, data):
        if not self.is_empty():
            temp = self.start
            if temp.item == data:
                self.delete_first()
                return
            temp = temp.next
            while temp != self.start:
                if temp.item == data:
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next
                    if temp == self.start.prev:
                        self.start.prev = temp.prev
                    return
                temp = temp.next
            if self.start.item == data:
                self.delete_last()

    def __iter__(self):
        return CDLLIterator(self.start)

class CDLLIterator:
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

# Testing the corrected code
cdll = CDLL()
cdll.insert_last(10)
cdll.insert_last(20)
cdll.insert_last(30)
cdll.insert_first(0)

cdll.print_list()  # Output: 0 10 20 30

cdll.delete_first()
cdll.print_list()  # Output: 10 20 30

cdll.delete_item(20)
cdll.print_list()  # Output: 10 30

cdll.delete_last()
cdll.print_list()  # Output: 10
 