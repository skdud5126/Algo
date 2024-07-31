'''
종이 꽃가루가 들어있는 풍선이 NXM 크기의 격자판에 붙어있는데,
어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터진다고 한다.
다음의 경우 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.

NXM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택해 터뜨렸을 떄 날릴 수 있는 꽃가루 수 중 최댓값을 출력하는 프로그램을 만드시오.
(3 <= N, M <= 100)


'''

T = int(input())  # 테스트 케이스 수 T
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


for case in range(1, T+1):
    N, M = map(int, input().split())  # N X M 입력 받음
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 입력받음
    max_value = 0   # 터트렸을 때 최댓값 넣어줄 초기 변수 설절

    for i in range(N):
        for j in range(M):   # 모든 원소 접근
            s = 0   # 각 원소에서 상,하,좌,우 꽃가루가 터졌을 때 더할 변수 초기값 설정
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= ni < M:   # 각 행과 열의 범위 벗어 나는 좌표 아닐 경우만 더해줌
                    s += arr[ni][nj]   # 상하좌우 다 더해줌
            res = arr[i][j] + s  # 자기자신도 더해줌
            if max_value < res:
                max_value = res

    print(f'#{case} {max_value}')