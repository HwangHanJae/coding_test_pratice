import sys


n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
#중복을 제거하기 위하여 집합 자료구조를 활용
sets = sorted(set(array))
#집합 자료구조로 index를 찾으면 시간초과가 나기 때문에
#딕셔너리 형태로 자료구조를 변경
array_dict = {}
for i, value in enumerate(sets):
    array_dict[value] =i
for number in array:
    print(array_dict[number], end=' ')