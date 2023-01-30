import sys
def solution(maps):
    sys.setrecursionlimit(10 ** 5)
    rows = len(maps)
    columns = len(maps[0])
    visited = [[False for _ in range(columns)] for _ in range(rows)]
    global total
    total = 0
    def dfs(x, y):
        global total
        visited[x][y] = True
        dx = [1,-1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < rows and 0 <= ny < columns):
                continue
            if visited[nx][ny]:
                continue
            if maps[nx][ny] == 'X':
                continue
            total += int(maps[nx][ny])
            dfs(nx, ny) 
    result = []
    for i in range(rows):
        for j in range(columns):
            if maps[i][j] != 'X' and visited[i][j] != True:
                total = int(maps[i][j])
                dfs(i, j)
            
                result.append(total)
    if len(result) > 0:
        return sorted(result)
    else:
        return [-1]
