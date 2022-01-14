n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort(reverse=True)
coins = []
for i in range(n):
    if k >= data[i]:
        coins.append(data[i])
count = 0
for coin in coins:
    count = count + k // coin
    k = k % coin
print(count)
