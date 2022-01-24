import sys


lstack = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())



rstack = []
for _ in range(n):
    data = sys.stdin.readline().rstrip().split()
    if len(data) == 2:
        if data[0] == "P":
            lstack.append(data[1])
    else:
        if data[0] == "L":
            if len(lstack) > 0:
                rstack.append(lstack.pop())
            
        elif data[0] == "D":
            if len(rstack) > 0:
                lstack.append(rstack.pop())
            
        
        elif data[0] == "B":
            if len(lstack) > 0:
                lstack.pop()
            
array = lstack + rstack[::-1]
for i in array:
    print(i,end='')




