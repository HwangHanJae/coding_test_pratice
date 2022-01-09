def push(stack,value):
    return stack.append(value)
def pop(stack):
    if len(stack) == 0:
        return print(-1)
    else :
        pop = stack[-1]
        stack.pop()
        return print(pop)
def size(stack):
    return print(len(stack))
def empty(stack):
    if len(stack) == 0:
        return print(1)
    else :
        return print(0)
def top(stack):
    if len(stack) == 0:
        return print(-1)
    else :
       return print(stack[-1])

import sys

n = sys.stdin.readline().rstrip()
n = int(n)

stack = []
for i in range(n):
    values = sys.stdin.readline().rstrip()
    values = values.split()
    if len(values) == 2:
        values[1] = int(values[1])
    if values[0] == "push":
        push(stack, values[1])
    if values[0]=="pop":
        pop(stack)
    if values[0] == "size":
        size(stack)
    if values[0] == "empty":
        empty(stack)
    if values[0] == "top":
        top(stack)
