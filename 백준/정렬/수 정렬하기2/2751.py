import sys
input = sys.stdin.readline
#퀵소트 구현하기
def quick_sort(array, start, end):
    if start>=end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <=  array[pivot]:
            left+= 1
        while right> start and array[right] >= array[pivot]:
            right -=1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right -1)
    quick_sort(array, right+1, end)

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

quick_sort(data, 0, len(data)-1)
for i in data:
    print(i)