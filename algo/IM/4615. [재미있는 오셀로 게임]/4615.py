# SWEA. 4615 재미있는 오셀로 게임

'''


'''

N = int(input())  # 보드 크기

board = [[0]*N for _ in range(N)]   # 보드 배열

for i in range(N//2-1, N//2+1):   # 스타트 보드
    for j in range(N//2-1, N//2+1):
        if i==j :
            board[i][j] = 2
            continue
        board[i][j] = 1

