# SWEA 4834. [숫자 카드]. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1. [가장 먼 노드] ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )

다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  # 테스트 케이스 T

for case in range(1, T+1):
    N = int(input())  # 카드 장수 N
    ai = input()  # N개의 숫자 ai

    zero_arr = [0]*10 # 10개의 빈 배열 생성

    for i in ai:
        for j in range(len(zero_arr)):
            if int(i) == j:
                zero_arr[j] +=1

    max_count = 0
    max_idx = 0
    for x in range(len(zero_arr)-1,-1,-1):
        if max_count < zero_arr[x]:
            max_count = zero_arr[x]
            max_idx = x
    print(f'#{case} {max_idx} {max_count}')

