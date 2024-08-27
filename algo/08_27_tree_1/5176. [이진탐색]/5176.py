# SWEA. 5176 이진탐색

def tree(num):
    global node

    if num <= N:
        tree(num*2)
        graph[num]= node   # num : 해당 노드
        node+=1
        tree(num*2+1)

T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N = int(input())

    graph = [0] * (N+1)
    node = 1  # 시작 노드

    tree(node)
    res = graph[N//2]

    print(f'#{case} {graph[1]} {res}')