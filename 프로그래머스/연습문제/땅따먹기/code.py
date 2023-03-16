def solution(land):
    for i in range(1, len(land)):
    ### 첫번째 풀이
        for j in range(len(land[i])):
          max_k = 0
          for k in range(len(land[i-1])):
              if k != j:
                  max_k = max(max_k, land[i-1][k])
          land[i][j] += max_k
    ### 두번째 풀이
          land[i][j] += max(land[i-1][j+1:] + land[i-1][:j])
    ### 세번째 풀이
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
    return max(land[-1])
            