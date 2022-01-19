from collections import deque
#DFS
def dfs(graph,v,visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
#BFS
def bfs(graph,v,visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        value = queue.popleft()
        print(value, end=' ')
        for i in graph[value]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(1, m+1):
    node1, node2= map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    graph[node1].sort()
    graph[node2].sort()

visited = [False] * (n+1)
dfs(graph,start, visited)
print()
visited = [False] * (n+1)
bfs(graph,start, visited)