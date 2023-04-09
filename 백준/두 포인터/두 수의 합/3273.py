n = int(input())
a = list(map(int, input().split()))
x = int(input())
result = 0
a.sort()
left = 0
right = n-1
while left < right:
    sum_value = a[left] + a[right]
    if  sum_value == x:
        result += 1
        left+=1
    elif sum_value < x:
        left+=1
    else:
        right -=1
print(result)