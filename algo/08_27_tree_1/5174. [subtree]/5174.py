# SWEA. 5174 subtree

def pre(node):  # 전위 순회 ( 나 -> 왼 -> 오)
    global res
    if node!=0:   # 본인 먼저 탐색
        res+=1   # 노드 탐색했을 시 노드 카운트 +1. [가장 먼 노드]
        pre(graph[node][0])   # 왼쪽 탐색
        pre(graph[node][1])   # 왼쪽탐색하고나서 오른쪽 탐색


T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    E, N = map(int,input().split())  # E : 간선의 개수 / N : N을 루트노드 지정
    arr = list(map(int,input().split()))  # 부모 노드 자식 노드 연결

    graph = [[0, 0] for _ in range(E+2)]  # 문제에서 노드 번호 1번부터 E+1번까지 존재하기 때문에 [0,0]사용x안해서 E+2
    res=0  # 서브트리에 있는 노드 개수 카운트할 초기 변수 설정
    for i in range(len(arr)//2):
        p, c = arr[i*2], arr[i*2+1]
        if not graph[p][0]:  # 부모노드를 인덱스로 0: 왼쪽 노드 1. [가장 먼 노드] : 오른쪽 노드로 저장
            graph[p][0] = c
        else:
            graph[p][1] = c
    pre(N)
    print(f'#{case} {res}')