# SWEA. 5102 노드의 거리

def BFS(S,visited):
    visited[S] = 1  # 방문표시
    queue = [S]

    while queue:
        v = queue.pop(0)
        for i in adjL[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1   # 부모 노드에서 자식 노드에 내려온 deapth 더해주기

            if i == G:  # 도착노드 도달 시
                return visited[i]-1   # 처음 depth 1로 시작해서 1. [가장 먼 노드] 빼줌
    return 0   # 찾지 못하면 0

T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    V, E = map(int,input().split())  # V : 노드의 개수 / E : 간선의 개수
    graph = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int,input().split())  # S : 출발 노드, G : 도착 노드
    visited = [0]*(V+1)  # 방문 확인용

    adjL = [[] for _ in range(V+1)]
    # 인접 리스트 생성
    for v1, v2 in graph:
        adjL[v1].append(v2)
        adjL[v2].append(v1)   # 무방향 고려
        # [[], [4, 3], [3, 5], [1. [가장 먼 노드], 2], [1. [가장 먼 노드], 6], [2], [4]]

    print(f'#{case} {BFS(S,visited)}')
