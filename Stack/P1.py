from Stack import *

def delimiter_pair_is_valid(delimiter_pair):
    if delimiter_pair[0] == '(' and delimiter_pair[1] == ')': return True 
    if delimiter_pair[0] == '[' and delimiter_pair[1] == ']': return True 
    if delimiter_pair[0] == '{' and delimiter_pair[1] == '}': return True 
    return False

def check_x(formula):
    stack = Stack()
    left = ['(', '[', '{']
    right = [')', ']', '}']

    for i in formula:
        if i in left:
            stack.push(i)
            continue
        if i in right:
            if delimiter_pair_is_valid([stack.pop(), i]):
                continue
            else:
                return False

    return True if stack.isEmpty() else False

formula = "(A+B]-A NOK ((A+B)+(C-D)"

print(formula)

if check_x(formula):
    print("Ta certo")
else:
    print("Ta errado")

