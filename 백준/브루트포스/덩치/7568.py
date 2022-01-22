n = int(input())
array = []
for _ in range(n):
    array.append(tuple(map(int, input().split())))

results = []
for i in range(n):
    k = 1
    for j in range(n):
        p,q = array[i][0],array[i][1]
        x,y = array[j][0], array[j][1]
         #A가 B보다 덩치가 클때
        if x > p and y > q:   
            k += 1   
    results.append(k)

for i in range(len(results)):
    print(results[i], end=' ')