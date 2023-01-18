from collections import deque
def solution(s):
    result = 0
    s = deque(s)
    for i in range(len(s)):
        if check(s):
            result +=1
        f = s.popleft()
        s.append(f)
    return result

def check(s):
    stack = []
    dic = {"}" : "{", "]" : "[", ")" : "("}
    for i in range(len(s)):
        if s[i] == '{' or s[i] == "[" or s[i] == '(':
            stack.append(s[i])
        else:
            for b in dic:
                if s[i] == b:
                    if len(stack) > 0 and stack[-1] == dic[b]:
                        stack.pop()
                    else:
                        return False            

    if len(stack) == 0:
        return True
    else:
        return False
    
        
                
        