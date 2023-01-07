# Linked list 

class node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head = None
        
    def add_elm(self, data):
        new_node = node(data)        
        new_node.ref =  self.head
        print(new_node.ref)
        self.head = new_node
        
    def traverse(self): 
        if self.head == None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

ll1 = linkedlist()
ll1.traverse()
ll1.add_elm(45)
ll1.add_elm(4)
ll1.add_elm(5)
ll1.add_elm(67)
ll1.add_elm(45)
ll1.traverse()