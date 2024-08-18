# SWEA. 3499 [퍼펙트 셔플]

T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N = int(input())   # 카드 개수
    card = list(input().split())  # 셔플할 카드 리스트

    res = []  # 셔플한 결과 담아줄 리스트
    for i in range(N//2+(N%2)):   # 홀수 일때도 가능
        res.append(card[i])
        if N//2+(N%2) + i < N:  # 범위 벗어나는지 아닌지 확인
            res.append(card[N//2+(N%2) + i])

    print(f'#{case}', *res)




