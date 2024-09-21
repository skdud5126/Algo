# SWEA. 5178 [노드의 합]

'''
완전 이진 트리의 리프 노드에 1000이하의 자연수가 저장되어 있고, 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다고 한다.

다음은 리프 노드에 저장된 1. [가장 먼 노드], 2, 3이 주어졌을 때, 나머지 노드에 자식 노드의 합을 저장한 예이다.

N개의 노드를 갖는 완전 이진 트리의 노드 번호는 루트가 1번이 되며, 같은 단계에서는 왼쪽에서 오른쪽으로 증가, 단계가 꽉 차면 다음단계의 왼쪽부터 시작된다.

완전 이진 트리의 특성상 1번부터 N번까지 빠지는 노드 번호는 없다.

리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음, 지정한 노드 번호에 저장된 값을 출력하는 프로그램을 작성 하시오.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1. [가장 먼 노드]<=T<=50

다음 줄부터 테스트 케이스의 별로 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L이 주어지고, 다음 줄부터 M개의 줄에 걸쳐 리프 노드 번호와 1000이하의 자연수가 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for case in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(M)]

    tree = [0]*(N+1)

    for p,c in arr:   # [0, 0, 0, 3, 1. [가장 먼 노드], 2]
        tree[p] = c

    for i in range(N,-1,-1):
        if i//2>0:
            tree[i//2]+=tree[i]  # 부모 노드 인덱스 접근
    print(f'#{case} {tree[L]}')
