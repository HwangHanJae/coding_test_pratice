from collections import deque
def bfs(x, y, rain):
  dx = [0,0,-1,1]
  dy = [1,-1,0,0]
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  while q:
    cx, cy = q.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if is_range(nx, ny) and visited[nx][ny] == False and graph[nx][ny] > rain:
        visited[nx][ny] = True
        q.append((nx, ny))
  return True

def is_range(x, y):
  if (0 <= x < n) and (0 <= y < n):
    return True
  else:
    return False
  
  

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

#최대 높이 구하기
max_height = 1
for row in graph:
  for height in row:
    max_height = max(max_height, height)

#안전영역 구하기
safe = []
for rain in range(0, max_height+1):
  count = 0
  visited = [[False for _ in range(n)] for _ in range(n)]
  for x in range(n):
    for y in range(n):
        if graph[x][y] > rain and visited[x][y] == False:
          bfs(x,y,rain)
          count += 1
  safe.append(count)
print(max(safe))
