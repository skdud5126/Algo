# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

'''
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.

짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면,
이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.

예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고,
중간 페이지 c= int((l+r)/2)로 계산한다.

찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

A는 300, B는 50 쪽을 찾아야 하는 경우,
다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.

'''

import sys
sys.stdin = open("input.txt", "r")

def search(page, search_page):
    start, end = 1, page
    count = 0
    while start <= end:
        middle = (start+end)//2   # 중앙페이지
        count += 1
        if middle == search_page:
            return count
        elif middle > search_page:
            end = middle
        else:
            start = middle
    return count



T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    P, A, B = map(int, input().split())  # 전체 쪽수 P, 찾을 쪽 번호 Pa, Pb
    count_A = search(P, A)
    count_B = search(P, B)


    if count_A < count_B:
        print(f'#{case} A')
    elif count_A == count_B:
        print(f'#{case} 0')
    else:
        print(f'#{case} B')
