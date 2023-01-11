#Linked list

class node:
    def __init__(self, data):
        self.data = data
        self.ref = None
    
class linked_List:
    def __init__(self):
        self.head = None
    
    def insert_begining(self,data):
        n = node(data)
        n.ref = self.head
        self.head = n
        pass

    def insert_end(self,data):
        n = node(data)
        temp = self.head 
        while (True):
            if self.head.ref is None:
                self.head.ref = n
                break
            
            self.head = self.head.ref
        self.head = temp

    def delete(self):
        temp = self.head
        ref = self.head.ref
        self.head = self.head.ref
        temp.data = None
        temp.ref = None 

    def traverse(self):
        if self.head == None:
            print("Linked list is empty!")
        else :
            head = self.head
            print("<: | ",end="")
            while (True):
                if self.head == None:
                    print (":>")
                    break  
                print(self.head.data, end=" | ")
                self.head = self.head.ref                
            self.head = head

    def insert_after(self, n0 ,data ):
        n = node(data)
        temp = self.head
        t_ref = self.head.ref
        while self.head is not None:
            if self.head.data == n0 :
                n.ref = self.head.ref 
                self.head.ref = n
                break
            self.head = self.head.ref
        if self.head is None:
            print("node not present in list")
        self.head = temp
        self.head.ref = t_ref   

    def insert_before(self,node2,data):
        n = self.head
        node_ibw = node(data)
        if n.data == node2:
            node_ibw.ref = n
            self.head = node_ibw
        else :    
            while n is not None:
                if n.ref.data is node2:
                    node_ibw.ref = n.ref
                    n.ref = node_ibw
                    break
                n = n.ref
            if n is None:
                print ("node is not present")

llk = linked_List()
llk.insert_begining(10)
llk.insert_begining(45)
llk.insert_begining("jai")
llk.insert_begining("om")
llk.traverse()
llk.insert_end("mahadev")
llk.traverse()
llk.insert_begining(0)
llk.insert_end(90)
llk.traverse()
llk.delete()
llk.insert_begining("bom")
llk.traverse()
llk.delete()
llk.traverse()

llk2 = linked_List()
llk2.insert_begining("hariom")
llk2.traverse()
llk.insert_after("jai",50)
llk.insert_after(10,"har har")
llk.traverse()
llk2.insert_after(12,"yo yo")
llk.insert_before(50,"shree")
llk2.insert_before("hariom", "hari hari ")
llk2.traverse()
llk2.insert_before("hariom","narayan")
llk.traverse()
llk.insert_before(50,"shri Ram")
llk.traverse()
llk2.traverse()
