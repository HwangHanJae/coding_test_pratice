import sys

input = sys.stdin.readline

def binary_search(array,start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return 1
        elif target > array[mid]:
            start = mid + 1
        else :
            end = mid - 1
    return 0

results = []
n = int(input())
num_card = list(map(int, input().split()))
num_card = sorted(num_card)
m = int(input())
cards = list(map(int, input().split()))

for i in range(len(cards)):
    result = binary_search(num_card,0, n-1, cards[i])
    if i == len(cards)-1:
        print(result)
    else:
        print(result, end=' ')