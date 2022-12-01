def solution(chicken):
    result = 0
    while True:
        if chicken < 10:
            return(result)
        result += chicken // 10
        chicken = (chicken // 10) + (chicken % 10)
    