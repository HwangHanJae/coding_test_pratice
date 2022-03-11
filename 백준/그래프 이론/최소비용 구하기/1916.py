import sys
import heapq

def dijkstra(start):
  q = []
  distance[start] = 0
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

input = sys.stdin.readline
inf = 1e9

city = int(input())
bus = int(input())

graph = [[] for _ in range(city+1)]
distance = [inf] * (city+1)

for _ in range(bus):
  a,b,c = map(int, input().split())
  graph[a].append((b, c))

start, end = map(int, input().split())

dijkstra(start)
print(distance[end])