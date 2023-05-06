import collections
stack = collections.deque()

stack.append(99945999)
print (stack)
print (not stack)
stack.append(4545)
stack.append(63)
print(stack[-5])

import queue
stack = queue.LifoQueue(3)
stack.put(9)
stack.put(20)
stack.put(30)

stack.put(5)
print(stack.get(timeout=1))
