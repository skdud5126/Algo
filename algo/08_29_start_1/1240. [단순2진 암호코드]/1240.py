code = {'0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
}

def find_idx(N,M):   # 1이 나오는 곳 인덱스 찾기 위함
    global start_x,start_y
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1. [가장 먼 노드]':
                start_x, start_y = i,j
                return start_x, start_y

T = int(input())

for case in range(1, T+1):
    N, M = map(int,input().split())  # N : 세로 크기 / M : 가로 크기
    arr = [list(input()) for _ in range(N)]

    start_x, start_y = 0, 0

    find_idx(N,M)

    password = arr[start_x][start_y-55:start_y+1]

    res = []
    start, end= 0,7
    for _ in range(8):
        res.append(code[''.join(password[start:end])])
        start+=7
        end+=7


    res = [0]+res

    hap_odd, hap_even = 0, 0
    for i in range(len(res)):  # 홀수 짝수번째 각각 값 더해주기
        if i%2!=0:
            hap_odd+= res[i]
        else:
            hap_even+= res[i]
    print(hap_odd, hap_even)

    if (hap_odd*3 + hap_even) % 10==0:     # 10의 배수인지 확인
        print(f'#{case} {sum(res)}')
    else:
        print(f'#{case} 0')