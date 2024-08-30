T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N, M = map(int,input().split())  # 10 3
    v = list(map(int,input().split()))  # 1 2 3 4 5 6 7 8 9 10
    hap_li = [0]*(N-M+1)

    for i in range(N-M+1):
        for j in range(M):
            hap_li[i]+=v[i+j]

    print(f'#{case} {max(hap_li)-min(hap_li)}')



# 윈도우 슬라이싱 사용
# T = int(input())  # 테스트 케이스 수
#
# for case in range(1, T + 1):
#     N, M = map(int, input().split())  # 10 3
#     v = list(map(int, input().split()))  # 1 2 3 4 5 6 7 8 9 10
    # hap = sum(v[:M])
    # min_hap, max_hap = hap, hap
    #
    # for i in range(N-M):
    #     hap = hap - v[i] + v[i+M]
    #     min_hap, max_hap = min(min_hap,hap), max(max_hap,hap)
    #
    # print(f'#{case} {max_hap-min_hap}')