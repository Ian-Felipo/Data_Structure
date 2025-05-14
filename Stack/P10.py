from Stack import *

def invert_list(lista):
    stack = Stack()
    while len(lista) != 0: stack.push(lista.pop(0))
    while not stack.isEmpty(): lista.append(stack.pop())

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

invert_list(lista)

print(lista)