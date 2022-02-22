import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a,b))

# 정렬을 수행할 때, 첫번째 우선순위는 끝나는 시간으로 오름차순 정렬
# 두번째 우선순위는 시작 시간으로 오름차순을 정렬한다.
array = sorted(array, key=lambda x : (x[1], x[0]))


count = 1
end = array[0][1]
for i in range(1, n):
    if array[i][0] >= end:
        end = array[i][1]
        count += 1
print(count)

    
