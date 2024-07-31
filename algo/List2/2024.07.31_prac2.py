'''
5X5 2차 배열에 25개의 숫자를 저장하고,
25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
예를 들어 아래 그림에서 7값의 이웃한 값은 2, 6, 8, 12이며 차의 절대값의 합은 12이다.

25개의 요소에 대해서 모두 조사하여 총합을 구하시오.
벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주시하시오.
예를 들어 [0][0]은 이웃한 요소가 2개이다.
'''

T = int(input()) # 테스트 케이스 수

for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    total = 0
    for i in range(N):
        for j in range(N):  # NXN 배열의 모든 원소에 대해
            s = 0   # 문제에서 원소와 인접원소의 차의 ... 합 저장
            # i, j 원소의 4방향 원소에 대해
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    s += abs(arr[i][j] - arr[ni][nj])                # 실존하는 인접원소 ni, nj
            total += s
    print(f'#{case} {total}')
