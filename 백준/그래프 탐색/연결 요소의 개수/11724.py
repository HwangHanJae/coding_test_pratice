import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)

visited = [False] * (n+1)
results  = [True] * (n+1)
def bfs(start, visited):
  result = []
  q = deque()
  visited[start]
  q.append(start)
  while q:
    node = q.popleft()
    for i in graph[node]:
      if visited[i] ==False:
        visited[i] = True
        q.append(i)
  for i in range(len(visited)):
    if visited[i]:
      result.append(i)
  return tuple(result)

sets = set()
for i in range(1, n+1):
  temp = bfs(i, visited)
  if temp != ():
    sets.add(temp)
    
for i in sets:
  for j in i:
    results[j] = False

result = 0
for i in range(1,n+1):
  if results[i]:
    result+=1

result += len(sets)
print(result)