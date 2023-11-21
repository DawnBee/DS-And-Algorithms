def border():
	print("=============================","\n")

# Python program to
# demonstrate stack implementation
# using list

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

border()
# Python program to
# demonstrate stack implementation
# using collections.deque

from collections import deque

stack_d = deque()

# append() function to push
# element in the stack
stack_d.append('a')
stack_d.append('b')
stack_d.append('c')

print('Initial stack:')
print(stack_d)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack_d.pop())
print(stack_d.pop())
print(stack_d.pop())

print('\nStack after elements are popped:')
print(stack_d)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

border()
# Python program to
# demonstrate stack implementation
# using queue module

from queue import LifoQueue

# Initializing a stack
stack_m = LifoQueue(maxsize=3)

# qsize() show the number of elements
# in the stack
print(stack_m.qsize())

# put() function to push
# element in the stack
stack_m.put('a')
stack_m.put('b')
stack_m.put('c')

print("Full: ", stack_m.full())
print("Size: ", stack_m.qsize())

# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack_m.get())
print(stack_m.get())
print(stack_m.get())

print("\nEmpty: ", stack_m.empty())
