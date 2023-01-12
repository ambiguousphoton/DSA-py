class plate:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        
class stack:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        previous = self.head
        self.head = plate(data)
        self.head.next = previous
    
    def pop(self) :
        if self.head == None:
            print("stack is empty")
            return
        output = self.head.data
        self.head = self.head.next
        return output

    def show(self):
        n = self.head
        while n is not None:
            print(n.data)
            n  = n.next


stck = stack()
stck.push(45)
stck.push(20)
stck.push(14)
stck.push(51)

print(stck.pop())
print(stck.pop())
print("???????")
stck.show()
stck.pop()
print("///////")
stck.show()
stck.pop()
stck.pop()