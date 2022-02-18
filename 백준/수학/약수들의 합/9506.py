import sys

input = sys.stdin.readline

def solve(n):
    i = 1
    sets = set()
    while  i < n:
        if n % i ==0:
            sets.add(i)
            sets.add(n // i)
        i+=1
    results  = sorted(list(sets))[:-1]
    result = sum(sorted(list(sets))[:-1])
    return results, result

while True:
    n = int(input())
    if n == -1:
        break
    results, result = solve(n)
    if result == n:
        print("{} = ".format(n), end='')
        for i in range(len(results)):
            if i == len(results)-1:
                print("{}".format(results[i]))
            else:
                print("{} + ".format(results[i]), end='')
    else:
        print("{} is NOT perfect.".format(n))