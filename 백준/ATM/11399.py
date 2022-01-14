n = int(input())
data = list(map(int, input().split()))

data.sort()
result = data[0]
results = []
results.append(data[0])
for i in range(1, n):
    result = result + data[i]
    results.append(result)
print(sum(results))
