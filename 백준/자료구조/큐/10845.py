def push(queue, n):
    queue.append(n)
    return
def pop(queue):
    if len(queue) != 0:
        first = queue[0]
        queue.remove(first)
        print(first)
    else:
        print(-1)
def size(queue):
    print(len(queue))
def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)
def front(queue):
    if len(queue) != 0:
        print(queue[0])
    else:
        print(-1)
def back(queue):
    if len(queue) != 0:
        print(queue[-1])
    else:
        print(-1)

import sys
input = sys.stdin.readline
number = input().rstrip()
queue = []
for _ in range(int(number)):
    data = list(map(str, input().rstrip().split()))
    if data[0] == "push":
        push(queue, int(data[1]))
    elif data[0] == "front":
        front(queue)
    elif data[0] == "back":
        back(queue)
    elif data[0] == "size":
        size(queue)
    elif data[0] == "pop":
        pop(queue)
    elif data[0] == "empty":
        empty(queue)
