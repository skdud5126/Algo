'''
# 구간합(remake)

N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

제시된 길이와 같은 열방향 구간의 합이 가장 큰 경우와 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

***
[예시]

N = 5, M = 2

5, 3, 6, 1

1, 2

1, 2, 3

1

9, 0, 11

의 경우


    [5, 1], [1, 1], [1, 1], [1, 9]

    [3, 2], [2, 2], [2, 0]

    [6, 3], [3 ,11]
***
의 가능한 구간을 찾을 수 있다.

최대값이 나오는 경우와 그 합은: [3, 11], 14

최소값이 나오는 경우와 그 합은: [2, 0], 2

정답: 12

***
[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.

다음 줄부터 테스트 케이스의 첫 줄에 배열의 길이 N과 제약조건 M이 주어지고,

이후 N줄에 걸쳐 10,000 이하의 자연수가 주어진다.(연속된 같은 숫자가 주어지는 경우는 없다.)

***
[제약사항]

- 1 ≤ T ≤ 10
- 1 < N < 1,000
- 1 < M < 10
- 구간이 존재하지 않는 경우 -1 출력

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

1
5 2
5 3 6 1
1 2
1 2 3
1
9 0 11

'''

T = int(input())

for case in range(1,T+1):
    N, M = map(int,input().split())  # N : 배열 크기 / M : 이웃한 M개의 합
    arr = [list(map(int,input().split())) for _ in range(N)]
    length = 0  # 행의 최대 길이 구하기 위함
    ans = []  # 가능한 구간합 나타내기 위한 빈 리스트

    for li in arr:
        length = max(length, len(li))

    for i in arr: # 배열 돌면서 빈 곳 -1로 채워줌 0도 들어갈 수 있기 때문에 -1로 채움
        if len(i) < length:
            for _ in range(length-len(i)):
                i.append(-1)

    for col in range(length):  # 열 기준 -1아닌 값 res로 가져옴
        res = []  # [5, 1, 1, 1, 9] res
        for row in range(N):
            if arr[row][col]!= -1:
                res.append(arr[row][col])

        if len(res) < M:   # res 길이가 M보다 작으면 할 필요 X
            continue

        for i in range(len(res)-M+1):  # 구간합 구함
            hap = 0
            for m in range(M):
                hap += res[i+m]
            ans.append(hap)   # [6, 8, 10, 20, 5, 9, 11, 9, 23]  가능한 구간합 나타냄

    if not ans:# 구간합이 존재하지않으면 -1 출력
        print(f'#{case} -1')
    else:
        print(f'#{case} {max(ans)-min(ans)}')
