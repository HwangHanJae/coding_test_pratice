n = int(input())
count = 0
i = 1
while n:
  if i > n:
    i = 1
  n -= i
  count += 1
  i += 1
print(count)