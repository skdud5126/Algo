# SWEA. 21674. [미로] [파이썬 S/W 문제해결 기본] 5일차 - 미로


'''

NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오.

도착할 수 있으면 1. [가장 먼 노드], 아니면 0을 출력한다.

주어진 미로 밖으로는 나갈 수 없다.

다음은 5x5 미로의 예이다.

13101

10101

10101

10101

10021


마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.


[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1. [가장 먼 노드]<=T<=50

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다.

 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 1. [가장 먼 노드] 또는 0을 출력한다
'''

# import sys
# sys.stdin = open('input.txt',  'r')



# def find_xy(N,val,arr):    # 출발, 도착 위치 반환 하는 함수
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == val:   # 출발, 도착 좌표 반환
#                 return i,j

# for case in range(1. [가장 먼 노드], T+1. [가장 먼 노드]):
#     N = int(input())   # 미로의 크기 N
#     arr = [list(map(int,input())) for _ in range(N)]    # NxN 미로 배열
#     visited = [[0]*N for _ in range(N)]   # NXN 빈배열 생성 방문 기록 용
#     stack = []
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != arrive_val:  # 도착 지점 3 아닐때
#                 continue
#
#             visited[i][j] = 1. [가장 먼 노드]   # 도착지점 3인 곳에 방문 1. [가장 먼 노드] 표시
#             for dx, dy in dxy:
#                 nx = i + dx
#                 ny = j + dy
#                 if nx < 0 or  nx >= N or ny < 0  or ny >= N: # 범위 벗어나는 곳 좌표 제외
#                     continue
#                 if arr[nx][ny] == 0 and visited[nx][ny] == 0:   # 통로(0)이고 방문하지 않은 곳이면 좌표 이동
#                     stack.append([nx,ny])    # 이동경로 스택에 추가
#                     i, j = nx, ny  # 좌표 이동


dxy = [[1,0], [-1,0], [0,-1], [0,1]]   # 하, 좌, 우, 상 방향 좌표 설정

T = int(input())   # 테스트 케이스 수 T

start_val = 2    # 출발
arrive_val = 3   # 도착

def dfs(x,y,visited):
    global result  # 전역변수 수정 위함

    visited[x][y] = 1  # 방문한 곳 1로 표시
    for dx,dy in dxy:  #  도착지점 기준으로 좌표 이동
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 범위 벗어나는 것 제외
            continue
        if maze_arr[nx][ny] == 2:   # 좌표 이동 후 마지막 기점에서 상하좌우 탐색했을 때 2 발견하면 함수 종료
            result = 1
            return
        elif maze_arr[nx][ny] == 0 and visited[nx][ny] == 0:   # 통로(0) 존재하고 방문한적 없는곳 탐색
            dfs(nx,ny,visited)
    return  # 다돌았는데 2를 찾지못하면 함수 종료

for case in range(1, T+1):
    N = int(input())   # 미로의 크기 N
    maze_arr = [ list(map(int,input())) for _ in range(N)]   # NXN 미로 배열
    visited = [[0]*N for _ in range(N)]   # NxN 빈 배열 생성
    result = 0   # 결과 초기값 설정

    for i in range(N):
        for j in range(N):
            if maze_arr[i][j] != arrive_val:    # 도착지점 찾음
                continue
            dfs(i,j,visited)  # 3인 곳 찾아 거기서부터 dfs함수 호출
            print(f'#{case} {result}')
