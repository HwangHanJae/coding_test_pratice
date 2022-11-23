def solution(cacheSize, cities):
    cache = []
    result  = 0 
    for city in cities:
        #도시를 모두 소문자로 만들어줌
        city = city.lower()
        #캐시의 크기가 0이면 도시 수만큼 5를 더해줌
        if cacheSize == 0:
            result += 5
        else:
            #도시가 캐시에 존재하는 경우
            if city in cache:
                result += 1
                #캐시가 꽉찬 경우
                if len(cache) >= cacheSize:
                    #해당 도시를 제거하고 다시 맨 뒤로 채움
                    cache.remove(city)
                    cache.append(city)
                #캐시에 자리가 있는경우
                else:
                    cache.append(city)
            else:
                result += 5
                #캐시가 꽉찬 경우
                if len(cache) >= cacheSize:
                    #가장 오래된 도시를 제거하고 현재 도시를 맨뒤로 채움
                    cache.pop(0)
                    cache.append(city)
                else:
                    cache.append(city)
    return result
                
            