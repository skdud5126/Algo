# SWEA. 1226 [S/W 문제해결 기본] 7일차 - 미로1
dxy = [[0,1], [1,0], [0,-1], [-1,0]]

def BFS(x,y):
    queue = []
    queue.append([x,y])
    visited[x][y] = 1
    res = 0
    while queue:
        x, y = queue.pop()

        for dx, dy in dxy:
            nx , ny = x + dx, y + dy
            if 0<=nx<box_size and 0<=ny<box_size and miro[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append([nx,ny])
                visited[nx][ny]=1
            elif miro[nx][ny] == 3:
                res = 1
                break
        if res == 1 or not queue:
            break
    return res

for _ in range(1, 11):
    case = int(input())  # 테스트 케이스 번호
    box_size = 16
    miro = [list(map(int,input())) for _ in range(box_size)]
    visited = [[0]*box_size for _ in range(box_size)]

    for i in range(box_size):
        for j in range(box_size):
            if miro[i][j] == 2:  # start
                x, y = i, j
                break
    res = BFS(x,y)
    print(f'#{case} {res}')