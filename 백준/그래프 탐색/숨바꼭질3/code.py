from collections import deque

n, k = map(int, input().split())

q = deque()
q.append((n, 0))
visited = set()
visited.add(n)
while q:
    x, d = q.popleft()
    if x == k:
        break
    for next_x in [2*x, x-1, x+1]:
        if next_x not in visited and 0 <= next_x <= 100000:
            visited.add(next_x)
            if next_x != 2*x:
                q.append([next_x, d+1])
            else:
                q.append([next_x, d])
        
print(d)