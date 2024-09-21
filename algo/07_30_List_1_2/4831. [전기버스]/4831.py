# SWEA. 4831 [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

'''
A도시는 전기버스를 운행하려고 한다.

전기버스는 한 번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한 번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다.

출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함되지 않는다.

다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1. [가장 먼 노드], 3, 5, 7, 9인 경우의 예이다.

[입력]

첫 줄에 노선 수 T가 주어진다.  ( 1. [가장 먼 노드] ≤ T ≤ 50 )

각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1. [가장 먼 노드] ≤ K, N, M ≤ 100 )

[출력]

#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.
'''



T = int(input())   # 노선 수

for case in range(1, T+1):
    K, N, M = map(int,input().split())  # K : 한 번 충전시 갈 수 있는 최대 거리/ N : N개의 정류장 / M : 충전기 설치 대수
    elec_notion = list(map(int,input().split()))  # 충전기 설치된 정류장 배열

    notion = [0]+elec_notion+[N]  # 시작 0에서부터 정류장 끝까지 탐색
    start = 0
    res = 0
    for i in range(1,M+2): # M 정류소 보다 시작과 끝 정류장 추가한만큼의 범위 설정
        if notion[i] - notion[i-1] > K:   # K만큼 이동 못하면 종료 조건 설정  K = 3 인데 [0, 10, 12] 이면 3만큼 이동 불가
            res = 0
            break
        if notion[i] - start > K:  # K만큼 커지면 그 전 충전기 설치된 곳에서 충전해야함
            start = notion[i-1]  # start값 그 전 인덱스로 다시 재할당
            res += 1  # 충전 횟수 count
    print(f'#{case} {res}')



    # res = []
    # for i in range(M-1. [가장 먼 노드]):
    #     if elec_notion[i]<=K:
    #         cnt = 0
    #         for j in range(i+1. [가장 먼 노드], M):
    #             if elec_notion[j] - elec_notion[j-1. [가장 먼 노드]] > K:
    #                 res = 0
    #                 break
    #             if elec_notion[j-1. [가장 먼 노드]]+K >= elec_notion[j]:
    #                 cnt += 1. [가장 먼 노드]
    #         res.append(cnt)
    #
    # print(f'#{case} {min(res)}')


