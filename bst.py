class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item = item 
        self.right = right 
        self.left = left 


class BST:
    def __init__(self):
        self.root = None
    def insert(self,data):
        self.root = self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left,data)
        elif data > root.item:
            root.right = self.rinsert(root.right,data)
        return root 
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item == data:
            return root 
        if data < root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
    def inorder(self):
        result = []
        self.rinorder(self.root,result)
        return result 
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):
        result = []
        self.rpreorder(self.root,result)
        return result 
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    def postorder(self):
        result = []
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
    def min_val(self,temp):
        current = temp 
        while current.left is not None:
            current = current.left 
        return current.item 
    def max_val(self,temp):
        current = temp 
        while current.right is not None:
            current = current.right 
        return current.item
    def delete(self,data):
        self.root = self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root 
        if data < root.item:
            root.left = self.rdelete(root.left,data)
        elif data > root.item:
            root.right = self.rdelete(root.right,data)
        else:
            if root.right is None:
                return root.left 
            elif root.right is None:
                return root.right 
            temp = self.max_val(root.left)
            root.item = temp 
            root.left = self.rdelete(root.left,temp)
        return root 
    def size(self):
        return len(self.inorder())

tree = BST()

# Insert some data
tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(3)
tree.insert(7)

# Traverse the tree before deletion
print("Inorder before delete:", tree.inorder())

# Delete a node
tree.delete(5)
# Traverse the tree after deletion
print("Inorder after delete:", tree.inorder())