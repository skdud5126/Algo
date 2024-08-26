# SWEA. 5102 노드의 거리

def BFS(S,visited):
    global res

    visited[S] = True  # 방문표시
    queue = [S]
    if S != G:
        res += 1
    while queue:
        v = queue.pop(0)

        for i in adjL[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

        if G != adjL[v]:
            res+=1
        else:
            return

T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    V, E = map(int,input().split())  # V : 노드의 개수 / E : 간선의 개수
    graph = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int,input().split())  # S : 출발 노드, G : 도착 노드
    res = 0
    visited = [False]*(V+1)  # 방문 확인용

    adjL = [[] for _ in range(V+1)]
    # 인접 리스트 생성
    for v1, v2 in graph:
        adjL[v1].append(v2)
        adjL[v2].append(v1)   # 무방향 고려
        # [[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]

    BFS(S,visited)
    print(f'#{case} {res}')
