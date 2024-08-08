# SWEA. 2805 농작물 수확하기

T = int(input())  # 테스트 케이스 T

for case in range(1, T+1):
    N = int(input())  # 농장 크기 N
    arr = [list(map(int, input().split())) for _ in range(N)]

    hap = 0
    for i in range(N):
        if i <= N // 2:   # 중앙을 기점으로 바꿔줌
            for j in range(N//2-i, N//2+i+1):
                hap += arr[i][j]
        else:
            for j in range(i-N//2,N//2+i+1):
                hap += arr[i][j]
    print(f'{case} {hap}')