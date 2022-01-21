def d(n):
    result = 0
    for i in range(len(str(n))):
        result += int(str(n)[i])
    result += n
    return result

n = 1

results = set()
while n < 10000:
    results.add(n)
    n+=1

numbers = set()
a = 1
while a < 10000:
    numbers.add(d(a))
    a+=1
result = results.difference(numbers)
result = sorted(result)
for i in result:
    print(i)