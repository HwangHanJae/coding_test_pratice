import sys
import heapq


def solve(start, end, n):
  distance = [inf] * (n+1)
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))
  while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
      continue
    for n, c in graph[node]:
      cost = dist+c
      if cost < distance[n]:
        distance[n] = cost
        heapq.heappush(q, (cost, n))
  return distance[end]
input = sys.stdin.readline
inf = 1e9

n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
v1, v2 = map(int, input().split())


result1 = solve(1, v1,n) + solve(v1, v2,n) + solve(v2, n,n)
result2 = solve(1, v2,n) + solve(v2, v1,n) + solve(v1, n,n)

result = min(result1, result2)
if result >= inf:
  print(-1)
else:
  print(result)