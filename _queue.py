class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self,data):
        n = node(data)
        if self.front is None:
            self.front = n
            self.back = self.front
            return
        if self.front.next is None:
            self.back = n
            self.front.next = self.back   
            self.back.previous = self.front
            return

        back = self.back   
        self.back = n
        self.back.previous = back
        self.back.previous.next = self.back
        
    def dequeue(self):
        if self.front is None:
            print("queue is empty!")
            return
        output = self.front
        self.front = self.front.next
        return output.data

    def peek(self):
        return self.front.data

    def show(self):
        n = self.front
        while n is not None :
            print(n.data)
            n = n.next

q = queue()
q.enqueue(66)
q.enqueue(223)
q.enqueue("sifi")
q.enqueue("jai")
q.enqueue(6)
print(q.front.next.previous.data)
print("........................")
q.show()
print(q.dequeue())
print(q.dequeue())
print(q.front.data)
print("............................................")
q.show()
print("............................................")
q2 = queue()
q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(3)
q2.enqueue(4)
q2.enqueue(5)
q2.enqueue(6)
q2.show()
print("............................................")
print(q2.peek())
q2.dequeue()
print(q2.peek())