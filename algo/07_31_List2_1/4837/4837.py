# SWEA 4837. 부분집합의 합

'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.


예를 들어 N = 3, K = 6 경우, 부분집합은 { 1. [가장 먼 노드], 2, 3 } 경우 1가지가 존재한다.




[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1. [가장 먼 노드] ≤ T ≤ 50 )


테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1. [가장 먼 노드] ≤ N ≤ 12, 1. [가장 먼 노드] ≤ K ≤ 100 )



[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  # 테스트 케이스 T
num_li = [_ for _ in range(1, 13)]

for case in range(1, T+1):
    N, K = map(int, input().split())  # 부분집합 원소의 수 N 부분집합의 합
    count_value = 0

    for i in range(1<<12):   # 모든 부분집합의 경우의 수 2**11
        li = []
        count = 0
        hap = 0
        for j in range(len(num_li)):   # 3
            if i & (1<<j):
                li.append(num_li[j])    # 부분집합
        for li_num in li:   # 각 부분집합의 갯수 & 합 구하기
            count+=1
            hap += li_num
        if count == N and hap == K:   # 만약 부분집합의 갯수 N과 일치하고 합이 K이면 갯수 더하기
            count_value+=1
    print(f'#{case} {count_value}')





