import sys
input = sys.stdin.readline
k =  input().rstrip()
k = int(k)
array = []
for _ in range(k):
    data = input().rstrip()
    if int(data) == 0:
        array.pop()
    else:
        array.append(int(data))


print(sum(array))
