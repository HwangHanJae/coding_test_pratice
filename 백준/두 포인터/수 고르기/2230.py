n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
s = 0
e = 0
min_num = int(1e10)
while s < n and e < n:
    diff = array[e] - array[s]
    if diff < m:
        e+=1
    else:
        min_num = min(min_num, diff)
        s+=1
print(min_num)