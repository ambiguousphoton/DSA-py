import linkedlist

def _reversed(llk):
    _link = llk.head
    head = llk.head.ref
    llk.head.ref = None
    while head is not None:
        link_ =  head.ref
        head.ref = _link
        _link = head
        head = link_
    llk.head = _link
    return llk.head

def start():
    llk = linkedlist.linked_List()
    llk.insert_begining(9)
    llk.insert_begining(8)
    llk.insert_begining(7)
    llk.insert_begining(6)
    llk.insert_begining(5)
    llk.insert_begining(4)
    llk.insert_begining(3)
    llk.insert_begining(2)
    llk.insert_begining(1)
    llk.traverse()
    _reversed(llk)
    llk.traverse()

    llk2 = linkedlist.linked_List()
    llk2.insert_begining("G")
    llk2.insert_begining("A")
    llk2.insert_begining("T")
    llk2.insert_begining("E")
    llk2.traverse()
start()