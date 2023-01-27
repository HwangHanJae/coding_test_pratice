def solution(record):
    texts =[]
    ids =[]
    user_info = {}
    result =[]
    for chat in record:
        data = chat.split()
        input_text = data[0]
        input_id = data[1]
        if input_text == 'Enter' or input_text == 'Change':
            user_info[input_id] = data[2]
        
        if input_text != 'Change':
            texts.append(input_text)
            ids.append(input_id)
    
    for text, id_ in zip(texts, ids):
        if text == 'Enter':
            result.append(user_info[id_] + "님이 들어왔습니다.")
        else:
            result.append(user_info[id_] + '님이 나갔습니다.')
            
    return result
            
        