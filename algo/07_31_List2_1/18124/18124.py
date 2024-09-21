# SWEA 18124. List2 - 연습문제2. 부분집합 합 문제 구현하기

''''
그럼 실제로 10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성해보자.
만약 합이 존재 하면 1. [가장 먼 노드], 그렇지 않으면 0을 출력하도록 한다.
'''

import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for case in range(1, T+1):
    arr = list(map(int, input().split()))   # 배열 전달받음
    li = []   # 부분집합 합 넣어줄 빈 배열
    for i in range(1,1<<len(arr)):   # 공집합 제외 모든 부분집합 생성 수
        subset = []    # 부분집합
        for j in range(len(arr)):
            if i & (1<<j):
                subset.append(arr[j])
        hap = sum(subset)  # 부분집합 합
        li.append(hap)
    if 0 in li:
        print(f&apos;#{case} 1. [가장 먼 노드]&apos;)
    else:
        print(f&apos;#{case} 0&apos;)