from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    while goal:
        if cards1:
            c1 = cards1.popleft()
        if cards2:
            c2 = cards2.popleft()
        g = goal.popleft()
        if g == c1:
            cards2.appendleft(c2)
        elif g == c2:
            cards1.appendleft(c1)
        else:
            return 'No'
    return 'Yes'