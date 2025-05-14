from Stack import *

def invert_stack(stack):
    aux = Stack()
    reverse_stack = Stack()

    while not stack.isEmpty():
        aux.push(stack.peek())
        reverse_stack.push(stack.pop())

    while not aux.isEmpty():
        stack.push(aux.pop())

    return reverse_stack

stack = Stack()

for i in range(10): stack.push(i)

print(stack)
print(stack)

reverse_stack = invert_stack(stack)

print(reverse_stack)


    
        



