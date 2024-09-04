# SWEA. 5207 [이진 탐색]


    # if start > end:
    #     return 0
    # else:
    #     if key == A_li[mid]:
    #         return key
    #     elif A_li[mid] < key:
    #         return aa(A_li, mid+1, end, key)
    #     else:
    #         return aa(A_li, start, mid-1, key)

def aa(A_li, start, end, key):
    global ans
    sign = 0   # 표식

    while start <= end :
        mid = (start + end) // 2

        if A_li[mid] == key:   # 해당 값 찾으면 카운트 해주고 함수 return
            ans +=1
            return
        elif A_li[mid] < key:  # 탐색 오른쪽 구역
            start = mid + 1
            if sign == 1:   # sign이 1이란 것은 그 전 탐색 구역이 오른쪽이라는 뜻 그럼 불가능 break
                break
            sign = 1
        else:
            end = mid - 1
            if sign == -1:
                break
            sign = -1
    return ans

T = int(input())

for case in range(1, T+1):
    N, M = map(int,input().split())  # N : A의 개수 / M : B의 개수
    A_li = list(map(int,input().split()))
    B_li = list(map(int,input().split()))

    A_li.sort()  # 정렬한 상태로 A리스트 저장

    start = 0  # 탐색 시작 지점 지정
    end = N - 1  # 탐색 끝 지점점 지정
    ans = 0
    for el in B_li:
        aa(A_li, start,end, el)

    print(f'#{case} {ans}')