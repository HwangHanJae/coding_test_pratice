from collections import deque, Counter
def solution(n, edge):
    def bfs(all_nodes):
        distance = {node : 0 for node in all_nodes}
        q = deque()
        q.append(1)
        while q:
            n = q.popleft()
            for node in graph[n]:
                if distance[node] == 0:
                    distance[node] = distance[n] + 1
                    q.append(node)
        distance[1] = 0
        return distance
    
    graph = {}
    all_nodes = set()
    for node in edge:
        if node[0] not in graph:
            graph[node[0]] = []
        if node[1] not in graph:
            graph[node[1]] = []
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
        all_nodes.add(node[0])
        all_nodes.add(node[1])
        
    distance = bfs(all_nodes)
    max_distance = max(distance.values())
    
    result = Counter(distance.values())[max_distance]
    
    
    return result
    
        
    
        