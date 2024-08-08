# 백트래킹 (미로)


def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

T = int(input())

for case in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input().split())) for _ in range(N)]


    # 출발위치 찾기
    sti, strj = fstart(N)

    visited = [[0]*N for _ in range(N)]