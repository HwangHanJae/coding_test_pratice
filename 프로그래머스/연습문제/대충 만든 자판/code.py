def solution(keymap, targets):
    mapping = {}
    for s in range(len(keymap)):
        for i, key in enumerate(keymap[s]):
            if key not in mapping:
                mapping[key] = mapping.get(key, i+1)
            mapping[key] = min(mapping.get(key), i+1)
    result = []
    for target in targets:
        sum_value = 0
        for c in target:
            if c not in mapping:
                result.append(-1)
                break
            sum_value += mapping[c]
        else:
            result.append(sum_value)
        
    return result