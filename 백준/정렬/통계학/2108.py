from collections import Counter
import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    data = int(sys.stdin.readline())
    array.append(data)

array = sorted(array)
#평균값 구하기
mean = round(sum(array) / len(array))
print(mean)

#중앙값 구하기
median = array[len(array)//2]
print(median)
#최빈값 계산하기
#최빈값을 계산하기 위해 Counter.most_common()을 사용
counter = Counter(array).most_common()
modes = []
for number, count in counter:
    if count == counter[0][1]:
        modes.append((number, count))
if len(modes) == 1:
    mode = modes[0][0]
else:
    modes = sorted(modes)
    mode = modes[1][0]
print(mode)

#범위 구하기
print(max(array) - min(array))