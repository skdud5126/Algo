# SWEA. 6485 삼성시의 버스 노선
import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #  테스트 케이스 수

for case in range(1, T+1):
    N = int(input())  # 버스 노선 갯수
    bus_routes = [list(map(int, input().split())) for _ in range(N)]  # [[1. [가장 먼 노드],3], [2,5]]
    P = int(input())  # 버스 정류장 갯수

    C = [int(input()) for _ in range(P)]  # 버스 정류장 번호   [1. [가장 먼 노드], 2, 3, 4, 5]

    bus_stop = [0]*5001  # 버스가 지나간 정류장 경로 확인용

    for A,B in bus_routes:
        for i in range(A-1,B):
            bus_stop[i] +=1

    print(f'#{case}', end = ' ')

    for i in C:   # 인덱스 번호 사용하여 값 들고옴
        print(f'{bus_stop[i-1]}', end= ' ')
    print()