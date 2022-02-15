import sys
input = sys.stdin.readline


n, k, l = map(int, input().split())

team_count = 0
vip_team = []
for _ in range(n):
    check = True
    team = list(map(int, input().split()))
    team_score = sum(team)
    for i in team:
        if i >= l:
            pass
        else:
            check = False
            break
    if check:
        if team_score >= k:
            check = True
            team_count+=1
            for i in team:
                vip_team.append(i)
        else:
            check = False

print(team_count)
for i in vip_team:
    print(i, end=' ')