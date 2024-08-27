# SWEA. 5176 이진탐색

def tree(num):
    if num < N:



T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N = int(input())

    graph = [[0,0] for _ in range(N+1)]

    # for i in range(1, N+1):
    #     for j in range(N//2,-1, -1):
    #         if not graph[2*(j-1)]:
    #             graph[2*(j-1)][0] = i

