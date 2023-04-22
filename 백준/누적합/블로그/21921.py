n, x = map(int, input().split())
array = list(map(int, input().split()))

prefix_sum = [0 for _ in range(n+1)]
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] +  array[i]

dic = {}
for i in range(len(array)+1-x):
    max_num = prefix_sum[i+x] - prefix_sum[i]
    dic[max_num] = dic.get(max_num, 0) + 1

result = sorted(dic.items(), key=lambda x : x[0], reverse=True)
if result[0][0] == 0:
    print('SAD')
else:
    print(result[0][0])
    print(result[0][1])
