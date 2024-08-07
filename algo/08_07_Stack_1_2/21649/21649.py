# SWEA. 21649 Stack1. 연습문제 3. 그래프 탐색(가장 먼저 풀어보기)

'''
* 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다. 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오. 시작 정점을 1로 시작하시오.
* 정점 탐색시 숫자가 낮은 정점부터 방문한다.

* 입력
총 테스트 갯수는 1개이며,
첫 줄은 정점의 개수(V)와 간선의 개수(E)이 주어지고,
그 다음 줄부터 간선의 개수 만큼 연결된 두 정점이 주어진다.

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7


* 출력 결과의 예는 다음과 같다.
#1 1-2-4-6-5-7-3

'''

# import sys
# sys.stdin = open('input.txt', 'r')

def DFS(s, V):
    stack = []
    visited = [0]*(V+1)  # 방문했는지 확인 용 
    visited[s] = 1
    
    v = s   # 확인용
    
    while True:
        for x in range(E):
            if visited[x] == 0:    # 방문한 기록이 없다면 stack에 추가
                stack.append(x)

for case in range(1):
    V, E = map(int,input().split())   # 정점의 개수 V 간선의 개수 E
    adjL = [[] for _ in range(V+1)]   # 인접리스트를 담기 위해 빈배열 생성
    arr = list(map(int, input().split()))  # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]  # 입력 받은 연결된 정점들 한짝씩 가져옴
        adjL[v1].append(v2)   # 각 정점과 연결된 정점들 추가
        adjL[v2].append(v1)   # 무방향이기때문에 서로서로 연결된 정점들 추가해줌
    # adjL = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
    
    
