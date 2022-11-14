def solution(board):
    b = []
    n = len(board)
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                b.append((i, j))
                
    for x, y in b:
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            #범위를 넘어가는 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                pass
            else:
                board[nx][ny] = 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                count += 1
    return count