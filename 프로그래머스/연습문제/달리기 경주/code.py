def solution(players, callings):
    player_rank = {}
    rank_player = {}
    for rank, player in enumerate(players):
        player_rank[player] = rank+1
        rank_player[rank+1] = player
    
    for calling in callings:
        #추월한 선수의 현재 등수
        rank = player_rank[calling]
        #추월당하는 선수의 이름
        overtaken = rank_player[rank-1]
        #추월한 선수의 등수 교체
        player_rank[calling] = rank-1
        rank_player[rank-1] = calling
        #추월당한 선수의 등수 교체
        player_rank[overtaken] = rank
        rank_player[rank] = overtaken
    
    result = [rank_player[i] for i in range(1, len(players)+1)]
        
    return result
        
        
        
        
            