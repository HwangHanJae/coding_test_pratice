n, k = map(int, input().split())
array = list(map(int, input().split()))
prefix_sum = [0]
result = []
sum_value = 0
for i in range(n):
    sum_value += array[i]
    prefix_sum.append(sum_value)

for i in range(n-k+1):
    result.append(prefix_sum[i+k] - prefix_sum[i])
    
print(max(result))