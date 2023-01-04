def solution(skill, skill_trees):
    skill_dic = {}
    count = 0
    for i,s in enumerate(skill):
        skill_dic[s] = i
    for skill in skill_trees:
        users = [-1]
        for s in skill:
            try:
                number = skill_dic[s]
                if number-1 in users:
                    users.append(number)
                else:
                    break
            except:
                pass
        else:   
            count += 1
    return count
