# 4875 [미로1]

def dfs(miro, x,y):
    global res
    dxy = [[0,1], [1,0], [0,-1], [-1,0]]  # 우, 하, 좌, 상

    visited[x][y] = 1  # 방문 표시
    for dx,dy in dxy:
        nx, ny = x+dx, y+dy
        if miro[nx][ny] == 3:
            res = 1
            return
        if 0<=nx<box_size and 0<=ny<box_size and miro[nx][ny] == 0 and visited[nx][ny] == 0:
            dfs(miro, nx,ny)
    return res

box_size = 16

for _ in range(1,2):
    case = int(input())  # 테케 입력
    miro = [list(map(int,input())) for _ in range(box_size)]
    visited = [[0]*box_size for _ in range(box_size)]
    res = 0

    for i in range(box_size):
        for j in range(box_size):
            if miro[i][j] == 2:
                x, y = i, j
                break
    print(f'#{case} {dfs(miro, x, y)}')