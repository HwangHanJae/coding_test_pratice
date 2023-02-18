from collections import deque
n = int(input())
m = int(input())
graph = {i : [] for i in range(1, n+1)}

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(v):
  visited = {}
  friends = set()
  q = deque()
  q.append((v, 0))
  while q:
    i, depth = q.popleft()
    if depth <= 2:
      friends.add(i)
    nodes = graph[i]
    visited[i]= True
    for node in nodes:
      if visited.get(node, False) == False:
        visited[node] = True
        q.append((node, depth+1))
  return friends - {1}


friends=dfs(1)
print(len(friends))
