# SWEA 1209. [S/W 문제해결 기본] 2일차 - sum

'''
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

다음과 같은 5X5 배열에서 최댓값은 29이다.

[제약 사항]

총 10개의 테스트 케이스가 주어진다.

배열의 크기는 100X100으로 동일하다.

각 행의 합은 integer 범위를 넘어가지 않는다.

동일한 최댓값이 있을 경우, 하나의 값만 출력한다.

[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

'''

import sys
sys.stdin = open('input.txt','r')

N = 100
for _ in range(1, 11):
    case = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_hap = 0

    for i in range(N):  # 각 행별 합
        hap = 0
        for j in range(N):
            hap += arr[i][j]
        if max_hap < hap:
            max_hap = hap

    for col in range(N):  # 각 열별 합
        hap = 0
        for row in range(N):
            hap += arr[row][col]
        if max_hap < hap:
            max_hap = hap

    hap = 0
    for r in range(N):  # 각 정방향 대각선 합
        for c in range(N):
            if r==c:
                hap += arr[r][c]

    if max_hap < hap:
        max_hap = hap

    hap = 0
    for q in range(N):   # 각 역방향 대각선 합
        for z in range(N):
            if q == N-1-z:
                hap += arr[q][N-1-z]
        if max_hap < hap:
            max_hap = hap
    print(f'#{case} {max_hap}')


