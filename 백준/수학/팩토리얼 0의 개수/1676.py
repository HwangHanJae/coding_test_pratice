import sys
n = int(sys.stdin.readline())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
num = str(factorial(n))
count= 0
for i in range(len(num)-1, -1,-1):
    if num[i] == "0":
        count+=1
    else:
        break
print(count)
print(num)