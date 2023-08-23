class minstack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, data):
        self.stack.append(data)
        if not self.min_stack or self.min_stack[-1] > data:
            self.min_stack.append(data)
        elif self.min_stack:
            self.min_stack.append(self.min_stack[-1])
    
    def pop(self):
        self.stack.pop(-1)
        self.min_stack.pop(-1)
    
    def top(self):
        return self.stack[-1]
    
    def min(self):
        print (self.min_stack[-1])
        
        return self.min_stack[-1]
    
    def status_of_stacks(self):
        print (self.min_stack, self.stack)
        return (self.min_stack, self.stack)
    
stack = minstack()
stack.push(1)
stack.push(2)
stack.status_of_stacks()
stack.push(22)
stack.status_of_stacks()
stack.pop()
stack.status_of_stacks()