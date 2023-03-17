import re
def solution(files):
    for i in range(len(files)):
        file = files[i]
        numbers= re.findall('\d+', file)
        print(numbers)
        number = numbers[0]
        
        s = file.index(number)
        e = len(number)
        split_file = [file[:s], file[s:s+e], file[s+e:]]
        files[i] = split_file
    files = sorted(files, key=lambda x : [x[0].lower(), int(x[1])])
    
    
        
    result = [''.join(file) for file in files]
    return result