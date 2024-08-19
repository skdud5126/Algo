T = int(input())

swap = {0:1, 1:0}

for case in range(1, T+1):
    N = int(input())  # N개의 스위치
    light = list(map(int, input().split()))   # [1,1,0,0,1]
    start_light = [0] * N   # [0,0,0,0,0]
    res = 0

    for i in range(N):
        if start_light[i]!= light[i]:
            idx = i+1
            for j in range(N):
                if (j+1) % idx == 0:
                    start_light[j] = swap[start_light[j]]
            res+=1

    print(f'#{case} {res}')