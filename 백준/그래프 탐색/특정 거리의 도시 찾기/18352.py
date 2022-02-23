import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

q= deque()
def bfs(x, visited, k):
    result = []
    q.append([x, 0])
    visited[x] = True
    while q:
        node, dist = q.popleft()
        if dist == k:
            result.append(node)
            continue
        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                q.append((i, dist+1))
    return result

n, m, k, x = map(int,input().split())

graph = [[] for _ in range(n+1)]

visited = [False for _ in range(n+1)]

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)

result = bfs(x, visited, k)
result = sorted(result)

if len(result) == 0:
    print(-1)
else:
    for i in range(len(result)):
        print(result[i])
