'''
그림과 같이 인덱스가 있는 10X10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수
를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.



'''

T = int(input())  # 테스트 케이스 개수 T


for case in range(1, T+1):
    N = int(input())  # 칠할 영역의 개수 N
    li = [list(map(int, input().split())) for _ in range(N)]   # 칠할 영역 좌표 입력받음
    arr = [[0]*10 for _ in range(10)]   #  10X10 빈 배열 생성


    for i in range(N):

        for x in range(li[i][0], li[i][2]+1):     # 2 4
            for y in range(li[i][1], li[i][3]+1):  #  2 4
                arr[x][y] += li[i][-1]
        counts = 0
        for z in arr:
            for q in z:
                if q == 3:
                    counts+=1

    print(f'#{case} {counts}')





