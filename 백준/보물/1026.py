n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

array = b.copy()

array.sort()
a.sort(reverse=True)
s= 0
for i in range(n):
    s += a[i] * array[i]
print(s)
