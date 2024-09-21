# SWEA 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

'''
그림과 같이 인덱스가 있는 10X10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수
를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.


예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.

2

2 2 4 4 1. [가장 먼 노드]  ( [2,2] 부터 [4,4] 까지 color 1. [가장 먼 노드] (빨강) 으로 칠한다 )

3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )



[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1. [가장 먼 노드] ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )

다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )

color = 1. [가장 먼 노드] (빨강), color = 2 (파랑)



[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 테스트 케이스 개수 T


for case in range(1, T+1):
    N = int(input())  # 칠할 영역의 개수 N
    li = [list(map(int, input().split())) for _ in range(N)]   # 칠할 영역 좌표 입력받음
    arr = [[0]*10 for _ in range(10)]   #  10X10 빈 배열 생성


    for i in range(N):

        for x in range(li[i][0], li[i][2]+1):     # 2 4
            for y in range(li[i][1], li[i][3]+1):  #  2 4
                arr[x][y] += li[i][-1]
        counts = 0
        for z in arr:
            for q in z:
                if q == 3:
                    counts+=1

    print(f'#{case} {counts}')





