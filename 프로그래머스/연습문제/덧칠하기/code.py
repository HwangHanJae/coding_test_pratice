def solution(n, m, section):
    wall = [i+1 for i in range(n)]
    paint = set(wall) - set(section)
    count = 0
    for i in section:
        if i not in paint:
            roller = wall[i-1:i-1+m]
            paint.update(roller)
            count += 1
    return count