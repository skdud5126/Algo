

'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_num = arr[0]

    for i in range(N):
        if min_num > arr[i]:
            min_num = arr[i]

    max_num = arr[0]
    for i in range(N):
        if max_num < arr[i]:
            max_num = arr[i]

    print(f'#{tc} {max_num-min_num }')