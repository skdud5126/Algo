# SWEA 1954. 달팽이 숫자

'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

[제약사항]

달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


'''

import sys
sys.stdin = open("input.txt", "r")

# dxy = [[0,1], [1,0], [0,-1], [-1,0]]   # 우, 하, 좌, 상 방향으로 좌표 지정
#
# T = int(input())
#
# for case in range(1, T+1):   # case T
#     N = int(input())
#     res = [[0]*N for _ in range(N)]  # NXN 배열 생성
#     i, j = 0, 0  # 초기 좌표 지정(0,0)
#     vector = 0   # 방향 벡터 지정
#
#     for num in range(1, N**2+1):
#         res[i][j] = num   # 현재좌표 값 넣어줌
#
#         nx, ny = i + dxy[vector][0], j + dxy[vector][1]    # 방향 이동 좌표 지정
#
#         if 0<=nx<N and 0<=ny<N and res[nx][ny] == 0:   # 범위 벗어나지 않고 값이 없는 곳일 경우
#             i,j = nx, ny   # 이동한 좌표 재할당
#         else:
#             vector = (vector+1) % 4  # 범위 벗어나거나 좌표가 이미 지정된 경우 방향 전환
#             i += dxy[vector][0]
#             j += dxy[vector][1]
#     print(f'#{case}')
#
#     for elm in res:
#         print(' '.join(map(str, elm)))





dxy = [[0,1], [1,0], [0,-1], [-1,0]]  # 우 하 좌 상 방향

T = int(input())

for case in range(1, T+1):
    N= int(input())
    arr =  [[0]*N for _ in range(N)]
    x, y = 0, 0
    vector = 0

    for i in range(1, N**2+1):
        arr[x][y] = i

        nx , ny = x + dxy[vector][0], y + dxy[vector][1]
        if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            vector = (vector+1)%4
            x += dxy[vector][0]
            y += dxy[vector][1]

    print(f'#{case}')

    for k in arr:
        print(' '.join(map(str, k)))