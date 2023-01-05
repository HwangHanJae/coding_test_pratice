from itertools import combinations
def solution(orders, course):
    dic = {}
    result = []
    for n in course:
        dic[n] = {}
        for order in orders:
            for item in combinations(sorted(order), n):
                menu = ''.join(item)
                dic[n][menu] = dic[n].get(menu, 0) + 1
        result += [k for k, v in dic[n].items() if (max(dic[n].values()) == v) and (v >= 2)]
            
    result.sort()
    return result