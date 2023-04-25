def f(word, length):
    return word * length
s = input()
t = input()

if f(s, len(t)) == f(t, len(s)):
    print(1)
else:
    print(0)
