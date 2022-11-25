from itertools import permutations
def solution(k, dungeons):
    results = []
    for dungeon in permutations(dungeons, len(dungeons)):
        max_ = k
        result = 0
        for lst in dungeon:
            if max_ >= lst[0]:
                max_ -= lst[1]
                result +=1
            else:
                pass
        results.append(result)
    return max(results)