from collections import Counter
from queue import PriorityQueue
def solution(N, stages):
    counter = Counter(stages)
    users = len(stages)
    q = PriorityQueue()
    result = []
    for stage in range(1, N+1):
        if counter[stage] == 0:
            r = 0
        else:
            r = counter[stage] / users
        q.put((-r, stage))
        users -= counter[stage]
    
    for _ in range(q.qsize()):
        result.append(q.get()[1])
    return result