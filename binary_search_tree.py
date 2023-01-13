class Binary_search_tree():         
    def __init__(self,data):
        self._lchild = None
        self.rchild_ = None
        self.key = data


    def insert(self,data):
        if data is None : return
        if self.key == None:
            self.key = data
            return

        if self.key < data:
            if self.rchild_:
                self.rchild_.insert(data)
            else:
                self.rchild_ = Binary_search_tree(data)

        elif self.key > data:
            if self._lchild:
                self._lchild.insert(data)
            else:
                self._lchild = Binary_search_tree(data)

    def search(self,data):
        if self.key == data:
            print("node is present")
            return
    
        if self.key < data:
            if self.rchild_: 
                self.rchild_.search(data)
            else:
                print("node is not present")
        
        else :
            if self._lchild:
                self._lchild.search(data)
            else: 
                print("node is not present")
    
    def preorder_travelsal(self):
        print(self.key)
        if self._lchild:
            self._lchild.preorder_traversal()
        if self.rchild_:
            self.rchild_.preorder_travelsal()

list1 =[1,32,43,4,24,2,124,43,243,12,2423]
bst = Binary_search_tree(43)
for i in list1:
    bst.insert(i)

bst = Binary_search_tree(10)
bst.search(4)
print(".......................................................................")
bst.preorder_travelsal()