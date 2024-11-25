class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_first(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n    

    def insert_last(self, data):
        if self.is_empty():
            self.insert_first(data)
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n = Node(temp, data, None)        
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')               
            temp = temp.next
        print()  # for a new line after printing the list

    def delete_first(self):  
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.start is None:
            return
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next  
            temp.prev.next = None

    def delete_after(self, data):
        target = self.search(data)
        if target is not None and target.next is not None:
            target.next = target.next.next
            if target.next is not None:
                target.next.prev = target

    def __iter__(self):
        return DLLIterator(self.start)               

class DLLIterator:
    def __init__(self, start=None):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            data = self.current.item
            self.current = self.current.next
            return data

# # Example usage
# mylist = DLL()     
# mylist.insert_last(40)
# mylist.insert_first(10)                    
# mylist.insert_first(20)                    
# mylist.insert_first(30) 
# mylist.insert_after(mylist.search(20), 50)
# mylist.delete_after(30)

# for i in mylist:
#     print(i, end=' ')
# # Output: 30 20 50 10 40

