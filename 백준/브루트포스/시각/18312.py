n, k = map(int, input().split())

count = 0
for s in range(0, 60):
    for m in range(0, 60):
        for h in range(0, n+1):
            if h < 10:
                h = '0'+str(h)
            if int(m) < 10:
                m = '0'+str(m)
            if int(s) < 10:
                s = '0'+str(s)

            if str(k) in str(h):
                count += 1
            elif str(k) in str(m):
                count += 1
            elif str(k) in str(s):
                count += 1
print(count)