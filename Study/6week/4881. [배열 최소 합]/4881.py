# 4881. 배열 최소 합
def min_hap(x, sum_v):
    global min_sum

    if sum_v >= min_sum:
        return

    if x == N:
        if min_sum > sum_v:
            min_sum = sum_v
            return

    for col in range(N):
        if visited_row[col] == 0:
            visited_row[col] = 1
            min_hap(x+1, sum_v+arr[x][col])
            visited_row[col]=0



T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    visited_row = [0]*N  # 방문 행 표시
    min_sum = N*10

    min_hap(0,0)

    print(f'#{case} {min_sum}')