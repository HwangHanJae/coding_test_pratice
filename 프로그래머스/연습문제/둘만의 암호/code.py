def solution(s, skip, index):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in skip]
    alphabet_to_index = {}
    index_to_alphabet = {}
    for i, c in enumerate(alphabet):
        alphabet_to_index[c] = i
        index_to_alphabet[i] = c
    result = ''
    for c in list(s):
        i = (alphabet_to_index[c] + index) % len(alphabet)
        result += index_to_alphabet[i]

    return result
    
    
    
    
    
    