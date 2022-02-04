import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    stack = []
    check = True
    if s == ".":
        break
    for i in range(len(s)):
        if s[i] == ".":
            break
        else:
            if s[i] == "(" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == ")":
                if stack == [] or stack[-1] == "[":
                    check = False
                    break
                else:
                    stack.pop()
            elif s[i] == "]":
                if stack == [] or stack[-1] == "(":
                    check = False
                    break
                else:
                    stack.pop()
    if stack != []:
        check =False

    if check:
        print('yes')
    else :
        print('no')
