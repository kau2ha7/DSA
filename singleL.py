class Node:
    def __init__(self,item=None,next=None):
        self.item = item 
        self.next = next 

class SLlist:
    def __init__(self,start=None):
        self.start = start 
    def is_empty(self):
        return self.start is None 
    def insert_start(self,data):
        n = Node(data,self.start)
        self.start = n
    def insert_last(self,data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start 
            while temp.next is not None:
                temp = temp.next 
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
            n = Node(data,temp.next)
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
            if self.start.next is None:
                self.start = None
            else:
                self.start = self.start.next 
    def delete_last(self):
        if not self.is_empty():
            if self.start.next is None:
                self.start = None
            else:
                temp = self.start 
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None 
    def delete_item(self,data):
        if not self.is_empty():
            if self.start.next is None and self.start.item == data:
                self.start = None
            if self.start.item == data:
                self.delete_first()
            else:
                temp = self.start 
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next 
                        return
                    temp = temp.next 
    def __iter__(self):
        return SLLIterator(self.start)


class SLLIterator:
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
    
mylist = SLlist()
mylist.insert_last(40)
mylist.insert_start(10)                    
mylist.insert_start(20)                    
mylist.insert_start(30) 
mylist.insert_after(mylist.search(20), 50)
mylist.delete_first()
mylist.delete_last()
for i in mylist:
    print(i, end=' ')