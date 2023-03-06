def solution(wallpaper):
    lux, luy, rdx, rdy = 50, 50, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i+1)
                rdy = max(rdy, j+1)
    return lux, luy, rdx, rdy
                