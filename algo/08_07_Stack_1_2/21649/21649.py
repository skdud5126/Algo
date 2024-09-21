# SWEA. 21649 Stack1. 연습문제 3. 그래프 탐색(가장 먼저 풀어보기)

'''
* 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다. 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오. 시작 정점을 1로 시작하시오.
* 정점 탐색시 숫자가 낮은 정점부터 방문한다.

* 입력
총 테스트 갯수는 1개이며,
첫 줄은 정점의 개수(V)와 간선의 개수(E)이 주어지고,
그 다음 줄부터 간선의 개수 만큼 연결된 두 정점이 주어진다.

7 8
1. [가장 먼 노드] 2 1. [가장 먼 노드] 3 2 4 2 5 4 6 5 6 6 7 3 7


* 출력 결과의 예는 다음과 같다.
#1. [가장 먼 노드] 1. [가장 먼 노드]-2-4-6-5-7-3

'''

import sys
sys.stdin = open('input.txt', 'r')


def DFS(s, V):
    stack = []  # 방문한 정점 push할 stack
    res = []  # 탐색 경로 결과
    visited = [0]*(V+1)  # 방문했는지 확인 용 
    visited[s] = 1   # 방문한 곳 1로 표시
    v = s   # 확인용

    res.append(v)  # 경로 탐색 결과에 현재 정점 추가
    while True:
        for x in adjL[v]:     # 현재 정점과 연결된 인접정점 접근
            if visited[x] == 0:    # 방문한 기록이 없다면 stack에 추가
                stack.append(v)  # 현재 정점 stack에 추가
                v = x    # 현재 정점에서 인접정점으로 방문하여 재할당
                res.append(v)
                visited[x] = 1  # 현재 방문한 곳 표시
                break   # 가까운 for문 탈출
        else:    # for가 정상적으로 완료했을때 실행하는 구문
            if stack:   # 인접정점이 없다는 것 pop해서 되돌아감
                v = stack.pop()
            else:  # stack 비었으면 모두 방문했기에 break while문 탈출
                break
    return res


for case in range(1):
    V, E = map(int,input().split())   # 정점의 개수 V 간선의 개수 E
    adjL = [[] for _ in range(V+1)]   # 인접리스트를 담기 위해 빈배열 생성
    arr = list(map(int, input().split()))  # 1. [가장 먼 노드] 2 1. [가장 먼 노드] 3 2 4 2 5 4 6 5 6 6 7 3 7

    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]  # 입력 받은 연결된 정점들 한짝씩 가져옴
        adjL[v1].append(v2)   # 각 정점과 연결된 정점들 추가
        adjL[v2].append(v1)   # 무방향이기때문에 서로서로 연결된 정점들 추가해줌
    # adjL = [[], [2, 3], [1. [가장 먼 노드], 4, 5], [1. [가장 먼 노드], 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
    print(f'#{case+1} {"-".join(map(str,DFS(1,V)))}')

    
