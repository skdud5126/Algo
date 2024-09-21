# SWEA. 5431. [민석이의 과제 체크하기] 민석이의 과제 체크하기

'''
민석이는 교수가 되었고, 이번에 처음으로 맡은 과목에 수강생이 N명이다.

민석이는 처음으로 과제를 내었다.

그리고 제출한 사람의 목록을 받았다.

수강생들은 1번에서 N번까지 번호가 매겨져 있고, 어떤 번호의 사람이 제출했는지에 대한 목록을 받은 것이다.

과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 수강생의 수를 나타내는 정수 N(2≤N≤100)과 과제를 제출한 사람의 수를 나타내는 정수 K(1. [가장 먼 노드]≤K≤N)가 공백으로 구분되어 주어진다.

두 번째 줄에는 과제를 제출한 사람의 번호 K개가 공백으로 구분되어 주어진다. 번호는 1이상 N이하의 정수이며 같은 번호가 두 번 이상 주어지는 경우는 없다.


[출력]

각 테스트 케이스마다 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력한다.


'''

import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())  # 테스트 케이스 수
#
# for case in range(1. [가장 먼 노드], T+1. [가장 먼 노드]):
#     N, K = map(int,input().split())  # N : 수강생 수 , K : 과제 제출한 학생 수
#     submit_num = list(map(int, input().split()))   # 과제 제출한 번호
#
#     check_submit = [0]*(N+1. [가장 먼 노드]) # 냈는지 확인하기 위한 빈배열 생성
#
#     for i in range(K):
#         for j in range(1. [가장 먼 노드],N+1. [가장 먼 노드]):    # 학생 번호는 1부터 시작하기에 0은 제외 하여 순회
#             if submit_num[i] == j:   # 제출한 학생의 리스트 순회하면서 1. [가장 먼 노드]~5중에 같으면
#                 check_submit[j] = 1. [가장 먼 노드]   # check_submit 인덱스 활용하여 제출한 학생 번호(=인덱스)에 체크 "1. [가장 먼 노드]" 표시
#
#     print(f'#{case}' , end = ' ')
#
#     for not_chek in range(1. [가장 먼 노드],N+1. [가장 먼 노드]):
#         if check_submit[not_chek] == 0:  # 제출하지 않은 학생 인덱스 == 제출 안한 사람의 번호
#             print(not_chek, end = ' ')
#     print()


T = int(input())  # 테스트 케이스 수

for case in range(1 , T + 1):

    N, K = map(int, input().split())
    submit_num = list(map(int, input().split()))
    res = []  # 결과 담을 res
    check_num = [ _ for _ in range(1, N+1)]   # 학생 수 만큼 체크num 리스트 생성

    for i in check_num:  # 체크 넘 순회
        if i not in submit_num:   # 만약 제출한 숫자가 check에 없으면 res에 추가해줌
            res.append(i)

    print(f"#{case} {' '.join(map(str,res))}")