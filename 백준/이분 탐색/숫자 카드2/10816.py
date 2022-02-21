import sys

input = sys.stdin.readline

def binary_search(array,start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
    return None

n = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)

numbers_dict = {}

for i in numbers:
    if i not in numbers_dict:
        numbers_dict[i] = 1
    else:
        numbers_dict[i] += 1

m = int(input())
my_numbers = list(map(int, input().split()))

for my_num in my_numbers:
    mid = binary_search(numbers,0, n-1, my_num)
    if mid is not None and my_num == numbers[mid] :
        print(numbers_dict[my_num], end=' ')
    else:
        print(0, end=' ')
