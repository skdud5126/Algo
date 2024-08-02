# SWEA 1210. [S/W 문제해결 기본] 2일차 - Ladder1

import sys
sys.stdin = open('input.txt')

for _ in range(1,11):
    # 첫 번째 줄에 테스트케이스 몇번
    tc = int(input())
    # 100*100 2차원 리스트
    arr = [list(map(int, input().split())) for _ in range(100)]


    # 모든 시작점에서 출발해봄.
    # 그리고 도착지점(2)에 제대로 도착했다면, 그 시작점 반환.
    if data[0][j] == 0:
        continue
