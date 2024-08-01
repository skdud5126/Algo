def selection_sort(arr, N): # arr 정렬대상, N 크기
    for i in range(N-1): # 주어진 구간에 대해...기준위치값 i를 정하고
        min_idx = i   # 최솟값 위치를 기준위치로 가정
        for j in range(i+1, N):   # 남은 원소에 대해 실제 최솟값 위치 검색
            if arr[min_idx] > arr[j]:
                min_idx = j
            # 구간의 최솟값을 기준위치로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

A = [2, 7, 5, 3, 4]
B = [4, 3, 2, 1]
selection_sort(A, len(A))
selection_sort(B, len(B))

print(A)
print(B)


'''
SWEA 1966. 숫자를 정렬하자.

주어진 N길이의 숫자열을 오름차순으로 정렬하여 출력하라.

[제약사항]
N은 5 이상 50 이하이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N이 주어지고, 다음 줄에 N개의 숫자가 주어진다.

[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

'''

def sort_li(li,num):
    for i in range(num-1):
        m_index = i
        for j in range(i+1,N):
            if li[m_index] > li[j]:
                m_index = j
        li[i],li[m_index] = li[m_index], li[i]
    return ' '.join(map(str,arr))

T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f"#{case} {sort_li(arr, len(arr))}")