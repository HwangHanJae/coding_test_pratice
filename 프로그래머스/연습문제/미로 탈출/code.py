from collections import deque
def solution(maps):
    def is_range(x, y):
        if 0 <= x < n and 0 <= y < m:
            return True
        else:
            return False
    def find(start, end):
        visited = [[0 for _ in range(m)] for _ in range(n)]
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        q = deque()
        q.append((start['x'], start['y'], 0))
        while q:
            cx, cy, count = q.popleft()
            if cx == end['x'] and cy == end['y']:
                return count
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if is_range(nx, ny) and visited[nx][ny] == 0 and graph[nx][ny] != 'X':
                    q.append((nx, ny, count+1))
                    visited[nx][ny] = 1
        return -1
    graph = list(map(list, maps))
    n = len(graph)
    m = len(graph[0])
    S = {'x' : 0, 'y' : 0}
    L = {'x' : 0, 'y' : 0}
    E = {'x' : 0, 'y' : 0}
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 'S':
                S['x'] = x
                S['y'] = y
            elif graph[x][y] == 'L':
                L['x'] = x
                L['y'] = y
            elif graph[x][y] == 'E':
                E['x'] = x
                E['y'] = y
    
    c1 = find(S, L)
    c2 = find(L, E)
    if c1 == -1 or c2 == -1:
        return -1
    return c1 + c2
            
    
    
            
        
    

        
    
        
