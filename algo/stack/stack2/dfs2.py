# 01.dfs_practice_인접리스트

# graph : 그래프를 나타내는 인접 리스트
# start : 탐색을 시작할 정점
# visited : 방문한 정점을 저장하는 집합
# result : 탐색 경로를 저장하는 리스트

def dfs(graph, start, visted, result):
    visited.add(start)    # 현재 정점 방문했다고 표시
    result.append(start)   # 현재 정점을 탐색 경로에 추가
    for neighbor in graph[start]:   # 현재 정점의 모든 인접 정점에 대해
        if neighbor not in visted:   # 인접 정점이 아직 방문되지 않았다면
            dfs(graph, neighbor, visted, result)   # DFS 재귀 호출  A가 호출을 불렀고 밑으로 다 돌았을 경우 A로 거슬러 올라오는데 C는 방문했기때문에 재귀 종료

# 그래프 인접 리스트
graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'G'],
    'D' : ['B', 'F'],
    'E' : ['B', 'F'],
    'F' : ['D', 'E', 'G'],
    'G' : ['C', 'F']
}

start_vertex = 'A'
visited = set()    # 방문한 정점을 저장할 집합
result = []   # 탐색 경로를 저장할 리스트


dfs(graph, start_vertex, visited, result)

print(' '.join(result))