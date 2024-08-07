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

# import sys
# sys.stdin = open("input.txt", "r")

dxy = [[0,1], [1,0], [0,-1], [-1,0]]   # 우, 하, 좌, 상 방향으로 좌표 지정

T = int(input())  # 테스트 케이스 T

for case in range(1, T+1):

    N = int(input()) # N크기 배열 입력받음
    arr = [[0] * N for _ in range(N)]   # NXN 빈 배열 생성




    # for x in range(N):
    #     for y in range(N):
    #         for num in range(N):
    #             for dx,dy in dxy:
    #                 nx = x + dx
    #                 ny = y + dy
    #
    #                 if nx < 0 or nx >= N or ny < 0 or ny >= N:
    #                     continue
    #
    #                 arr[nx][dy] = num+1
    #                 N += N
    #             print(arr)
