import sys
from collections import deque

s = sys.stdin.readline().rstrip()

result = ''
stack = []
q = deque()
tag = False

for i in range(len(s)):
    if s[i] == "<":          
        while stack:
            result += stack.pop()
        q.append(s[i])
        tag = True
    elif s[i] == ">":
        q.append(s[i])
        tag = False
        while q:
            result += q.popleft()
    elif s[i] == " ":
        if not tag:
            while stack:
                result += stack.pop()
            result += " "
        else:
            q.append(s[i])
            while q:
                result += q.popleft()
    else:
        if not tag:
            stack.append(s[i])
        else:
            q.append(s[i])
while stack:
    result += stack.pop()
print(result)


