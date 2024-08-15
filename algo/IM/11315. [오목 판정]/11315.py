# SWEA. 11315 오목판정

'''
N X N 크기의 판이 있다. 판의 각 칸에는 돌이 있거나 없을 수 있다. 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.



[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)이 주어진다.

다음 N개의 줄의 각 줄에는 길이 N인 문자열이 주어진다. 각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.


[출력]

각 테스트 케이스 마다 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력한다.

# '''
import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) # 테스트 케이스 수

for case in range(1, T+1):
    N = int(input())  # 오목 크기
    arr = [list(input()) for _ in range(N)]

    dxy = [[0,1], [1,0], [1,1],  [1,-1]]  # 우, 하, 우하 방향 대각, 좌하 방향 대각
    res = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':  # 시작점

                for dx, dy in dxy:
                    cnt = 0  # 방향 설정
                    for num in range(5):   # 5개만 나와도 오목
                        nx, ny = i+(dx*num), j+(dy*num)
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':  # 범위 벗어나지 않고 방향따라 돌이 있는 경우
                            cnt += 1
                        else:
                            break
                    if cnt == 5:  # 5개면 오목
                        res = 'YES'
                        break

    print(f'#{case} {res}')
