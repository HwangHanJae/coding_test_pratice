import heapq
def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while True:
        a = heapq.heappop(scoville)
        if a >= K:
            return count
        if len(scoville) < 1:
            return -1
        b = heapq.heappop(scoville)
        c = a + (b * 2)
        heapq.heappush(scoville, c)
        count += 1
    
    