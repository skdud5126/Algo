# SWEA. 2001 파리퇴치

'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

아래는 N=5 의 예이다.

M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.

죽은 파리의 개수를 구하라!

예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.

[제약 사항]

1. [가장 먼 노드]. N 은 5 이상 15 이하이다.

2. M은 2 이상 N 이하이다.

3. 각 영역의 파리 갯수는 30 이하 이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,

다음 N 줄에 걸쳐 N x N 배열이 주어진다.

[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
import sys
sys.stdin=open('input.txt', 'r')

T = int(input())  #  테스트 케이스 수 T

for case in range(1, T+1):
    N, M = map(int, input().split())   # N : 모기 배열  M : 파리채 크기

    mosq = [list(map(int,input().split())) for _ in range(N)]   # 모기 배열
    max_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for m_r in range(M):   # 2
                for m_c in range(M):
                    kill += mosq[i+m_r][j+m_c]

            if max_kill < kill:
                max_kill = kill
    print(f'#{case} {max_kill}')