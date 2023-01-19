from collections import deque
def solution(priorities, location):
    temp = [(p, i) for i, p in enumerate(priorities)]
    temp = my_sort(temp)
    for i in range(len(temp)):
        if location == temp[i][1]:
            return i+1
    
def my_sort(temp):
    q =deque(temp)
    result = []
    while q:
        j, index = q.popleft()
        if any(j < value[0] for value in q):
            q.append((j, index))
        # for i in range(0, len(q)):
        #     if q[i][0] > j:
        #         q.append((j, index))
        #         break
        else:
            result.append((j, index))
    return result
                