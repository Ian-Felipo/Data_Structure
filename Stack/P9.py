from Stack import *

def clean_stack(stack):
    if stack.isEmpty(): return stack
    stack.pop()
    clean_stack(stack)

stack = Stack()

for i in range(88): stack.push(i)

clean_stack(stack)

if stack.head == None: print("Deu certo")
