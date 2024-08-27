# SWEA. 1231 [중위순회]

import sys
sys.stdin = open('input.txt')

def inorder(node):
    global res
    if node:
        inorder(arr[node-1][2])
        res+=arr[node-1][1]
        inorder(arr[node-1][-1])

for case in range(1, 11):
    N = int(input())  # 정점의 갯수 N
    arr = [list(input().split()) for _ in range(N)]
    res = ''

    for node in arr:
        if len(node)!=4:
            for zero in range(4-len(node)):
                node.append('0')
        for i in range(len(node)):
            if node[i].isdigit():
                node[i] = int(node[i])


    inorder(1)

    print(f'#{case} {"".join(res)}')

