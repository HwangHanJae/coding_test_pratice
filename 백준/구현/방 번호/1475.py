import sys
input = sys.stdin.readline


numbers = {}
for i in range(10):
    numbers[str(i)] = 0

n = list(input().rstrip().replace("6","9"))
for i in n:
    numbers[i] +=1
numbers['9'] = int(numbers['9'] / 2) + numbers['9'] % 2
result = numbers["0"]
for i in range(1, len(numbers)):
    result = max(numbers[str(i)], result)
print(result)