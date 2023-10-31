import collections
stack = collections.deque()

stack.append(9994599459)
print (stack)
print (not stack)
stack.append(4545)
stack.append(63)
print(stack[-5])

import queue
stack = queue.LifoQueue(3)
stack.put(9)
stack.put(30)


print(stack.get(timeout=1))
