from collections import deque
def solution(people, limit):
    boat = 0
    people = deque(sorted(people))
    while people:
        if len(people) == 1:
            boat += 1
            break
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            boat += 1
        else:
            people.pop()
            boat += 1
                

    return boat