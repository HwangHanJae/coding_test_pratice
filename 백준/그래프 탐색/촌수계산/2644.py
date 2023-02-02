n = int(input())
start, target = map(int, input().split())
m = int(input())
graph = {i : [] for i in range(1, n+1)}
for _ in range(m):
  p, c = map(int, input().split())
  graph[p].append(c)
  graph[c].append(p)
visited ={node : False for node in graph}

result = []
def dfs(v, count):
  if v == target:
    result.append(count)
  count += 1
  visited[v] = True
  nodes = graph[v]
  for node in nodes:
    if not visited[node]:
      dfs(node, count)

dfs(start, 0)

if len(result) == 0:
  print(-1)
else:
  print(result[0])

