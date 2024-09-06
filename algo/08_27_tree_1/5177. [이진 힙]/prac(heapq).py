from heapq import heappush

T = int(input())

for case in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    heap = []
    ans = 0
    for num in arr:
        heappush(heap,num)

    heap = [0]+heap  # [0, 2, 3, 5, 7, 4, 6]

    node = len(heap)-1  # 끝 노드 번호 인덱스 가져오려고 함

    while node:
        node //=2
        ans += heap[node]
    print(f'#{case} {ans}')

