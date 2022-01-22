n = int(input())

#자리수를 다 더하는 함수
#198 => 198 + 1+9+8 = result
def digits_sum(i):
    result = i
    array = list(str(i))
    for i in range(len(array)):
        result += int(array[i])

    return int(result)

result = set()
for i in range(1, n):
    if digits_sum(i) == n:
        result.add(i)

if len(result) == 0:
    print(0)
else:
    print(min(result))