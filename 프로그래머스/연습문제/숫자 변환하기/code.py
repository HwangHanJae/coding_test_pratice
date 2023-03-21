from collections import defaultdict, deque
def solution(x, y, n):
    if x == y:
        return 0
    d = defaultdict(lambda :0)
    q = deque([x])
    while q:
        x= q.popleft()
        for next_x in [x+n, x*2, x*3]:
            if next_x > y:
                continue
            if d[next_x] > d[x]+1 or d[next_x] == 0:
                d[next_x] = d[x] + 1
                q.append(next_x)
        
    if d[y] == 0:
        return -1
    else:
        return d[y]
    
        