import sys
from collections import deque


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = str(input().rstrip())
    n = int(input())
    q = deque()
    data = input().rstrip().replace("[","").replace("]","").split(",")
    for i in range(len(data)):
        if i != "":
            q.append(data[i])

    error =  False
    reverse = False
    for i in p:
        if i == "R":
            if reverse:
                reverse = False
            else:
                reverse = True
        else:
            if len(q) != 0 and q[0] != '':
                if reverse:
                    q.pop()
                else : 
                    q.popleft()
            else:
                error = True
                break    
    if error:
        print("error")
    else:
        if reverse:
            q.reverse()

        print("[", end='')
        for i in range(len(q)):
            if i == len(q)-1:
                print(str(q[i]), end='')
            else:
                print(str(q[i]),end=',')
        print("]")
    