def solution(dirs):
    cx = 0
    cy = 0

    moved = set()
    for d in dirs:
        if d == 'U':
            nx = cx
            ny = cy+1
        elif d == 'D':
            nx = cx
            ny = cy-1
        elif d == 'L':
            nx = cx-1
            ny = cy
        elif d =='R':
            nx = cx+1
            ny = cy
        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue
        moved.add((cx, cy, nx, ny))
        moved.add((nx, ny, cx, cy))
        cx = nx
        cy = ny
    return len(moved) // 2
            
            