import sys
from collections import deque
q = deque()
def push(value):
    q.append(value)
def front():
    if len(q) > 0:
        print(q[0])
    else:
        print(-1)
def back():
    if len(q) > 0:
        print(q[-1])
    else:
        print(-1)
def size():
    print(len(q))
def empty():
    if len(q) == 0:
        print(1)
    else:
        print(0)
def pop():
    if len(q) == 0:
        print(-1)
    else:
        value = q.popleft()
        print(value)
input = sys.stdin.readline
n = int(input().rstrip())
for _ in range(n):
    data = list(map(str, input().split()))
    if data[0] == "push":
        push(int(data[1]))
    elif data[0] == "front":
        front()
    elif data[0] == "back":
        back()
    elif data[0] == "size":
        size()
    elif data[0] == "empty":
        empty()
    elif data[0] == "pop":
        pop()