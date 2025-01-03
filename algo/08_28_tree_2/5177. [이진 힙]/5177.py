# SWEA. 5177 [이진 힙]

import sys
sys.stdin = open('input.txt')

# target = 삽입한 위치
def enqueue(target):   # 삽입을 위한 함수
    # 단순히 tree에 삽입 대상을 집어 넣는게 아니라
    # 삽입 한 후에, 부모노드와 내 노드의 크기를 비교해서
    # 부모 노드의 값이 내 노드 값보다 크다면, 위치 스왑
    while target//2:
        parent = target//2
        if tree[target] <= tree[parent]:
            tree[target], tree[parent] = tree[parent], tree[target]
        target = parent



T = int(input())
for tx in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    tree = [0]
    # tree = [0] * (N+1. [가장 먼 노드])   #  0번 노드 사용하지 않으므로 N+1. [가장 먼 노드]

    last_node = 0
    for item in arr:
        tree.append(item)
        last_node+=1
        enqueue(last_node)

    print(tree, last_node)