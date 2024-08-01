'''
9490. 풍선팡

종이 꽃가루가 들어있는 풍선이 M개씩 N개의 줄에 붙어있고, 어떤 풍선을 터뜨리면
안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임이 있다.

예를 들어 풍선에 든 꽃가루가 1개씩일 때, 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서
총 5개의 꽃가루가 날리게 된다.

NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력하는 프로그램을 만드시오.

(3<=N, M<=100)

[입력]

첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M,
이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.


[출력]

#과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다

'''


import sys
sys.stdin = open("input.txt", "r")

T = int(input())   # 테스트 케이스 T


for case in range(1, T+1):
    N, M = map(int, input().split())   # N 행 수 M열 수 입력받음
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 입력
    max_hap = 0    # 꽃가루 합 최댓값 초기값 설정

    for i in range(N):
        for j in range(M):
            hap = 0

            for num in range(arr[i][j]):
                di = [0, (num+1), 0, (-1-num)]
                dj = [(num+1), 0, (-1-num), 0]
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0<=ni<N and 0<=nj<M:
                        hap += arr[ni][nj]
            hap += arr[i][j]
            if max_hap < hap:
                max_hap = hap

    print(f'#{case} {max_hap}')

