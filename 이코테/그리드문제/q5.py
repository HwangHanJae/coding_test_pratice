n , m = map(int, input().split())
data = list(map(int, input().split()))

results = []
for i in range(n):
    a = data[i]
    for j in range(1, n):
        b = data[j]
        if a!= b:
            results.append((i,j))

result = 0
for a,b in results:
    if a < b:
        result+=1
print(result)