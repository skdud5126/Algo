# SWEA 19606. List2 - 연습문제 1-1 대각선 원소의 합 구학
'''
5x5 2차배열에 25개의 숫자를 저장하고, 대각선 원소의 합을 구하시오.
대각선 원소는 다음과 같은 위치의 원소를 나타낸다.

[입력]
첫 줄은 테스트 케이스 개수
테스트 케이스 별로 첫 줄은 배열(N x N)의 크기 N
다음 줄 부터는 N 줄의 배열 요소
[출력]
모든 대각선의 합을 출력

'''

import sys
sys.stdin = open("input.txt", "r")


T = int(input())  # 테스트 케이스 수

for case in range(1, T + 1):
    N = int(input())  # 배열 NXN의 크기 입력받음
    N_arr = [list(map(int, input().split())) for _ in range(N)]  # N 줄의 배열
    sum_1 = 0  # 대각선 \ 합
    sum_2 = 0  # 대각선 / 합
    res = 0

    for i in range(N):
        for j in range(N):
            if i == j:
                sum_1 += N_arr[i][j]
            if N - 1 - i == j:
                sum_2 += N_arr[i][j]

            if N % 2 != 0:  # N이 홀수이면 중앙 중복값 한 번 빼주기
                count_2 = N_arr[N // 2][N // 2]
                res = sum_1 + sum_2 - count_2
            else:
                res = sum_1 + sum_2
    print(f'#{case} {res}')