from collections import deque
import sys



n = int(sys.stdin.readline())
result = deque()
for _ in range(n):
    data = list(sys.stdin.readline().split())
    if len(data) == 2:
        if data[0] == "push_front":
            result.appendleft(int(data[1]))     
        elif data[0] == "push_back":
            result.append(int(data[1]))    
    else:
        if data[0] == "pop_front":
            if len(result) != 0:
                print(result.popleft())
            else:
                print(-1) 
        elif data[0] == "pop_back":
            if len(result) != 0:
                print(result.pop())
            else:
                print(-1)       
        elif data[0] == "size":
            print(len(result))   
        elif data[0] == "empty":
            if len(result) != 0:
                print(0)
            else:
                print(1)  
        elif data[0] == "front":
            if len(result) != 0:
                print(result[0])
            else:
                print(-1)
        elif data[0] == "back":
            if len(result) != 0:
                print(result[-1])
            else:
                print(-1)
           