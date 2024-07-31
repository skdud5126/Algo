'''

10
0 0 254 185 76 227 84 175 0 0

'''

T = int(input())  # 테스트 케이스 개수

for i in (1, T+1):
    N = list(map(int, input().split()))  # 건물의 개수 N
    for j in range(2,T-2):

        new_li = N[j-2:j+3]
        max_floor = new_li[0]
        for z in new_li:
            if max_floor < z:
                max_floor = z

       # print(new_li)