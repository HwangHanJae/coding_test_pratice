import sys
import heapq
from collections import deque

inf = 1e9

input =sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n+1)]
costs = [inf for _ in range(n+1)]



m = int(input())
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))
start, end = map(int,input().split())

temp = [start] * (n+1)
def solve(start):
  q = []
  costs[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if costs[now] < dist:
        continue
    for next, next_cost in graph[now]:
      cost = dist+next_cost
      if cost < costs[next]:
        costs[next] = cost
        temp[next] = now
        heapq.heappush(q, (cost, next))
        
solve(start)
result = deque()

value =end
while value != start:
  result.appendleft(value)
  value = temp[value]
result.appendleft(start)

print(costs[end])
print(len(result))
for i in result:
  print(i, end=' ')
