import sys


n = int(sys.stdin.readline())
array = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    array.append((int(age), name, i))

array = sorted(array, key=lambda x : (x[0], x[2]))
for age, name, i in array:
    print(age, name)