import sys


n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

stack = []
results = []
check = True
count = 1
for number in array:
    while count <= number:
        stack.append(count)
        results.append("+")
        count+=1
    if stack[-1] == number:
        stack.pop()
        results.append("-")
    else:
        check = False

if check == False:
    print("NO")
else:
    for result in results:
        print(result)