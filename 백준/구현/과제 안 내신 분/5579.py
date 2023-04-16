numbers = set([i+1 for i in range(30)])
for _ in range(28):
    numbers -= {int(input())}
for n in sorted(list(numbers)):
    print(n)