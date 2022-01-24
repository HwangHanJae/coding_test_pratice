import sys

def reverse_word(words):
    for i in range(len(words)):
        word = list(words[i])
        word.reverse()
        word.append(' ')
        for j in range(len(word)):
            print(word[j],end='')
    print()       

t = int(sys.stdin.readline())
for _ in range(t):
    words = list(map(str,sys.stdin.readline().split()))
    reverse_word(words)