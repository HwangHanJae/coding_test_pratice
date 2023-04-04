def solution(park, routes):
    def is_range(h, w):
        #범위 안에 없다면
        if h < 0 or w < 0 or h >= H or w >= W:
            return False
        #범위 안에 있다면
        return True
    
    H = len(park)
    W = len(park[0])
    move = {'E' : (0, 1), 'W' : (0, -1), "S" : (1, 0), 'N' : (-1, 0)}
    #시작(현재) 위치 찾기
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                ch = i
                cw = j
                break
                
    #탐색
    for route in routes:
        #다음 위치 갱신
        nh, nw = ch, cw
        op, n = route.split()
        dh, dw = move[op]
        for _ in range(int(n)):
            #조건 부합한지 확인
            if is_range(nh+dh, nw+dw) and park[nh+dh][nw+dw] != 'X':
                nh += dh
                nw += dw
            else:
            #조건에 부합하지 않다면 초기화
                nh = ch
                nw = cw
                break
        #위치 갱신
        ch, cw = nh, nw
    return [ch, cw]

                
                    
        
                
                
        

            
    