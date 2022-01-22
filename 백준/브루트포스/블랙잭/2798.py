n, m = map(int, input().split())
numbers = list(map(int, input().split()))

#모든 경우의 수 구하기

sets = set()
for i in range(len(numbers)):
    for j in range(len(numbers)):
        for k in range(len(numbers)):
            #같은 인덱스인 경우만 피하기
            if i == j:
                pass
            elif j == k:
                pass
            elif k == i:
                pass
            else:
               value = numbers[i] + numbers[j] + numbers[k]
               if value <= m:
                sets.add(value)
array = list(sets)
array.sort(reverse=True)
print(array[0])