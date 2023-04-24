speak = ['pi', 'ka', 'chu']
s = input()
for word in speak:
    s = s.replace(word, 'A')
if set(s) == set('A'):
    print('YES')
else:
    print("NO")