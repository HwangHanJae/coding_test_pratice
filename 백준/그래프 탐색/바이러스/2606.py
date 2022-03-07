import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)

visited = [False] *(n+1)

def solve(start):
  q = deque()
  visited[start] = True
  q.append(start)
  while q:
    node = q.popleft()
    for i in graph[node]:
      if visited[i] == False:
        visited[i] = True
        q.append(i)
  return 


solve(1)
result = 0
for i in range(1,n+1):
  if i !=1 and visited[i]:
    result+=1
print(result)
