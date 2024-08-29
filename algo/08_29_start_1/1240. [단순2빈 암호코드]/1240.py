code = {'0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
}

T = int(input())

for case in range(1, T+1):
    N, M = map(int,input().split())  # N : 세로 크기 / M : 가로 크기
    arr = [list(input()) for _ in range(N)]

    start_x, start_y = 0, 0

    for i in range(N):
        for j in range(M):
            if arr[i][j]=='1':
                start_x, start_y = i, j

    print(start_x, start_y)