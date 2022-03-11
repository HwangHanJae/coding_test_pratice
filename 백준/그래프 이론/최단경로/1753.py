import sys
import heapq
input = sys.stdin.readline
inf = 1e9
distance = []
def short_path(start):
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for (n, c) in graph[now]:
      cost = dist + c
      if cost < distance[n]:
        distance[n] = cost
        heapq.heappush(q, (cost, n))


v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v+1)]
distance= [inf] * (v+1)
for _ in range(e):
  a, b, cost = map(int, input().split())
  graph[a].append((b, cost))


short_path(start)
for i in range(1, v+1):
  if distance[i] == inf:
    print("INF")
  else:
    print(distance[i])