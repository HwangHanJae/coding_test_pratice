from collections import deque
def solve(scores):
    #정렬
    scores = sorted(scores)
    scores = deque(scores)
    #최고점 최저점 제거
    scores.pop()
    scores.popleft()
    
    if scores[-1] - scores[0] >= 4:
        return 'KIN'
    else:
        return sum(scores)

t = int(input())
for _ in range(t):
    scores = list(map(int, input().split()))
    print(solve(scores))