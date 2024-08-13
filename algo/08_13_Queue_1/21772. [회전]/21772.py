# SWEA. 21772 [파이썬 S/W 문제해결 기본] 6일차 - 회전

'''
N개의 숫자로 이루어진 수열이 주어진다.

맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 첫 줄에 N과 M이 주어지고, 다음 줄에 10억 이하의 자연수 N개가 주어진다. 3<=N<=100, N<=M<=1000,

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.
'''
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N, M = map(int,input().split())  # N : 숫자 갯수 M : 회전하는 횟수
    num_list = list(map(int, input().split()))   # 숫자 리스트

    for m in range(M):
        num_list.append(num_list.pop(0))
    print(f'#{case} {num_list[0]}')