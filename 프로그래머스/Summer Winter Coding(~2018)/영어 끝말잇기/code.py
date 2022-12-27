def solution(n, words):
    turn = 1
    speaker = 1
    word_list = []
    for i in range(len(words)):
        if i== 0:
            pass
        else:
            pre_word=words[i-1]
            cur_word = words[i]
            word_list.append(pre_word)
            if pre_word[-1] != cur_word[0]:
                return [speaker,turn]
            elif cur_word in word_list:
                return [speaker, turn]
        if speaker == n:
            speaker = 1
            turn +=1
        else:
            speaker += 1
    return [0, 0]