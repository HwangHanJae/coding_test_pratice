# 첫 번째 방법
from collections import deque
def solution(msg):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic = {}
    for i, c in enumerate(alphabet):
        dic[c] = i+1
    
    result = []
    msg = deque(msg)
    while msg:
        for i in range(len(msg), 0, -1):
            word = ''.join(list(msg)[:i])
            if dic.get(word) != None:
                result.append(dic[word])
                add_word = ''.join(list(msg)[:i+1])
                dic[add_word] = len(dic) + 1
                break
        for _ in range(len(word)):
            msg.popleft()
    return result

# 두 번째 방법
def solution(msg):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic = {}
    for i, c in enumerate(alphabet):
        dic[c] = i+1
    
    result = []
    while True:
        #전체 단어가 딕셔너리에 등록되어 있는 경우
        if dic.get(msg):
            result.append(dic[msg])
            break
        for i in range(1, len(msg)+1):
            s = msg[:i]
            # 딕셔너리에 없을 경우
            if dic.get(s) == None:
                #이전 단어
                p = msg[:i-1]
                #이전단어를 딕셔너리에서 찾아서 결과로 등록
                result.append(dic[p])
                #현재 단어를 새롭게 등록
                dic[s] = len(dic) + 1
                msg = msg[i-1:]
                break
    return result