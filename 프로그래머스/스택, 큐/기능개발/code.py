from collections import deque
def solution(progresses, speeds):
    pair = zip(progresses, speeds)
    pair = deque(pair)
    stack = []
    result = []
    while pair:
        progress, speed = pair.popleft()
        remainder = 100 - progress
        x,y = divmod(remainder, speed)
        if y > 0:
            x +=1
        if stack != [] and stack[-1][0] >= x:
            a, b = stack.pop()
            stack.append((a, b+1))
        else:
            stack.append((x, 1))
    result = [i for _, i in stack]
    return result