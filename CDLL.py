class Node:
    def __init__(self,item=None,next=None,prev=None):
        self.item = item 
        self.next = next 
        self.prev = prev 

class CDLL:
    def __init__(self,start=None):
        self.start = start 
    def is_empty(self):
        return self.start is None
    def insert_first(self,data):
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
            self.start = n
    def insert_last(self,data):
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
    def search(self,data):
        if not self.is_empty():
            temp = self.start 
            while True:
                if temp.item == data:
                    return temp 
                temp = temp.next 
                if temp == self.start:
                    return
        return None 
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(prev=temp,item=data,next=temp.next)
            temp.next.prev = n
            temp.next = n
    def print_list(self):
        if not self.is_empty():
            temp = self.start 
            while True:
                print(temp.item,end=' ')
                temp = temp.next 
                if temp == self.start:
                    return
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
        while True:
            if temp.item == data:
                if temp == self.start:
                    self.delete_first()
                elif temp == self.start.prev:
                    self.delete_last()
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                return  # Exit after deleting the node
            temp = temp.next
            if temp == self.start:
                break  # Exit if we've looped through all nodes

    def __iter__(self):
        return CDLLIterator(self.start)
    
class CDLLIterator:
    def __init__(self,start=None):
        self.current = start 
        self.start = start 
        self.count = 0
    def __iter__(self):
        return self 
    def __next__(self):
        if self.current is None or (self.current == self.start and self.count ==1):
            raise StopIteration
        if self.current == self.start:
            self.count = 1
        data = self.current.item 
        self.current = self.current.next 
        return data 
    
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
 

