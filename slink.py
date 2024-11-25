class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLlist:
    def __init__(self, start=None):
        self.start = start        

    def is_empty(self):
        return self.start is None   

    def insert_start(self, data):
        n = Node(data, self.start) 
        self.start = n

    def insert_last(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
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
            n = Node(data, temp.next)                   
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    def delete_first(self):
        if self.start is not None:
            data = self.start.item
            self.start = self.start.next   
            return data 

    def delete_last(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, data):
        if self.start is None:
            return
        if self.start.item == data:
            self.start = self.start.next
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.item == data:
                    temp.next = temp.next.next
                    return
                temp = temp.next
    
    def __iter__(self):
        return SLliterator(self.start)

class SLliterator:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.start:
            raise StopIteration
        data = self.start.item
        self.start = self.start.next
        return data    

# Example usage
# mylist = SLlist()
# mylist.insert_last(40)
# mylist.insert_start(10)                    
# mylist.insert_start(20)                    
# mylist.insert_start(30) 
# mylist.insert_after(mylist.search(20), 50)
# mylist.delete_first()
# mylist.delete_last()
# for i in mylist:
#     print(i, end=' ')
