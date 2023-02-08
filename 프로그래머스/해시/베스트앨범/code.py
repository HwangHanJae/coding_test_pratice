def solution(genres, plays):
    hash = {}
    result = []
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in hash:
            hash[genre] = {}
            hash[genre]['detail'] = []
        hash[genre]['total'] = hash[genre].get('total', 0) + play
        hash[genre]['detail'].append((i, play))
    
    best_genres = []
    for genre in hash.keys():
        best_genres.append((genre, hash[genre]['total']))
        hash[genre]['detail'].sort(key=lambda x : x[1], reverse=True)
    best_genres.sort(key=lambda x: x[1], reverse=True)
    best_genres = [i[0] for i in best_genres]
    
    for genre in best_genres:
        index = [i[0] for i in hash[genre]['detail'][:2]]
        result += index
    return result