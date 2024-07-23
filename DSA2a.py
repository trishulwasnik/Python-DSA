#----------------------DSA--------------------------
#----------------------STACK------------------------
#-->Last In First Out(LIFO)
#-->another type of stack with new function of Deque from Collections
from collections import deque
stack=deque()
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

print(stack)
stack.pop()
stack.pop()
print(stack)
