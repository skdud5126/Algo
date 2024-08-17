# SWEA 9489. [고대 유적]

T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(M)]  # NXM 배열 입력
    max_res = 2  # 유물 크기 최소 크기 설정

    for row in range(N):   # 행방향 순으로 탐색
        cnt = 0
        for col in range(M):
            if arr[row][col]:   # 유물 있음
                cnt += 1
                continue
            if not arr[row][col] and cnt > max_res:  # 탐색하다 유물이 없고 2보다 크면  max 값 갱신
                max_res = cnt
                cnt = 0   # 다시 처음부터 시작
        if max_res < cnt:  # max값 갱신
            max_res = cnt

    for row in range(N):   # 열방향으로 순회 탐색  위랑 같은 원리
        cnt = 0
        for col in range(M):
            if arr[col][row]:   # 유물 있을 때까지 탐색
                cnt += 1
                continue
            if not arr[row][col] and cnt > max_res:
                max_res = cnt
                cnt = 0
        if max_res < cnt:
            max_res = cnt

    print(f'#{case} {max_res}')


