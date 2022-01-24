import sys


n = int(sys.stdin.readline())
for _ in range(n):
    data = list(sys.stdin.readline().rstrip())
    stack = []
    for i in range(len(data)):
        if data[0] == ")":
            stack.append(data[0])
            break
        else:
            if data[i] == "(":
                stack.append(data[i])
            elif data[i] == ")":
                if len(stack) == 0:
                    stack.append(data[i])
                    break
                else:
                    stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")