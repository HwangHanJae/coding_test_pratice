from collections import deque
def solution(prices):
    q = deque(prices)
    result = []
    while q:
        c = q.popleft()
        i = 1
        for p in q:
            if p < c:
                result.append(i)
                break
            i+=1
        else:
            result.append(len(q))
    return result