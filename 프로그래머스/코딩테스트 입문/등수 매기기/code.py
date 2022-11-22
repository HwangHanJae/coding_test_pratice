def solution(score):
    rank_dic = {}
    rank = []
    means = []
    result = []
    for e, m in score:
        mean = (e + m) / 2
        rank_dic[mean] = rank_dic.get(mean, 0)
        rank.append(mean)
        means.append(mean)
        
    rank.sort(reverse=True)
    
    for i in range(len(rank)):
        if rank_dic[rank[i]] == 0:
            rank_dic[rank[i]] = i+1
        else:
            pass
        
    for mean in means:
        result.append(rank_dic[mean])

    return result