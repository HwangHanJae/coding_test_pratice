def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())

parent = [0] * (v+1)
edges = []

for i in range(1, v+1):
  parent[i] = i

for i in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()

result = 0
last = 0
def kruskal(edges, result, last):
  for edge in edges:
    cost, a, b,  = edge
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b)
      result += cost
      last = cost
  return result, last

result_cost, last_cost = kruskal(edges, result, last)
print(result_cost - last_cost)
