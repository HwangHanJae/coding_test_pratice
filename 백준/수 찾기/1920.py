#1920문제 - 수 찾기
#이진 탐색 알고리즘
def binary_search(array, start, end, target):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return 0

n = int(input())
array_1 = list(map(int,input().split()))
m = int(input())
array_2 = list(map(int, input().split()))

array_1.sort()

for i in array_2:
    print(binary_search(array_1, 0, n-1, i))
