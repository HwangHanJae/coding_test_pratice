h, m = map(int, input().split())
def clock(h, m):
    minus = 45
    m = m-45
    if m < 0:
        m = m + 60
        h = h -1
    elif m >= 60:
        m = m - 60
        h = h+1
    if h < 0:
        h = h+24
    return h, m
hour, minute = clock(h, m)
print(hour, minute)