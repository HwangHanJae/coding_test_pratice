import sys
sys.setrecursionlimit(10**7)
def dfs(x, y):
  dx = [1,-1,0,0,1,1,-1,-1]
  dy = [0,0,1,-1,1,-1,1,-1]
  if x < 0 or y < 0 or x >= h or y >= w:
    return False
  if graph[x][y] == 1 and visited[x][y] == False:
    visited[x][y] = True
    for i in range(8):
      nx = dx[i] + x
      ny = dy[i] + y
      dfs(nx,ny)
    return True
  return False

while True:
  w, h = map(int, input().split())
  if (w, h) == (0, 0):
    break
  graph = []
  visited = [[False] * (w+1) for _ in range(h+1)]
  for _ in range(h):
    graph.append(list(map(int, input().split())))
  result = 0
  for i in range(h):
    for j in range(w):
      if dfs(i ,j):
        result+=1
  print(result)

