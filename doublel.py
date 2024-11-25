class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item 
        self.next = next 
        self.prev = prev 

class DLL:
    def __init__(self):
        self.start=None
    def is_empty(self):
        return self.start is None 
    def insert_first(self,data):
        n = Node(prev=None,item=data,next=self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start = n
    def insert_last(self,data):
        if self.is_empty():
            self.insert_first(data)
        else:
            temp = self.start 
            while temp.next is not None:
                temp = temp.next 
            n = Node(prev=temp,item=data,next=None)
            temp.next = n
    def search(self,data):
        if not self.is_empty():
            temp = self.start 
            while temp is not None:
                if temp.item == data:
                    return temp 
                temp = temp.next 
        return None 
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(prev=temp,item=data,next=temp.next)
            # if temp.next is not None:
            temp.next.prev = n
            temp.next = n
    def print_list(self):
        if not self.is_empty():
            temp = self.start 
            while temp is not None:
                print(temp.item,end=' ')
                temp = temp.next 
        print()
    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next 
            if not self.is_empty():
                self.start.prev = None
    def delete_last(self):
        if not self.is_empty():
            if self.start.next is None:
                self.start = None
            else:
                temp = self.start 
                while temp.next is not None:
                    temp = temp.next 
                temp.prev.next = None 
    def delete_after(self,data):
        temp = self.search(data)
        if temp is not None and temp.next is not None:
            temp.next = temp.next.next 
            if temp.next is not None:
                temp.next.prev = temp 
    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self,start=None):
        self.current = start 
    def __iter__(self):
        return self 
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item 
        self.current = self.current.next 
        return data 
    
mylist = DLL()
mylist.insert_last(40)
mylist.insert_first(10)
mylist.insert_first(20)
mylist.insert_first(30)
mylist.insert_after(mylist.search(20), 50)
mylist.delete_after(30)

for i in mylist:
    print(i, end=' ')