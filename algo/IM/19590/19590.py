# SWEA 19590.

'''
NXN 사각형의 전투장에는 각 칸마다 몇마리의 몬스터가 있는지 적혀 있다.
광대한 영역에 마법을 시전할 수 있는 마법사 Mort는 전투장에서 최대한 많은 몬스터를 잡으려 한다.

마법사 Mort는 대각선 방향으로 각 방향마다 K만큼 마법을 시전할 수 있다.

마법은 마법사가 있는 지점에서 마법을 시전한 위치를 제외하고 대각선 방향으로 방향 변화없이 시전된다.

예를 들어 5X5 인 전투장에서

    1. [가장 먼 노드]  2  3  5  10
    9  7  2  2  9
    0  0  1. [가장 먼 노드]  5  7
    5  2  3  2  2
    1. [가장 먼 노드]  1. [가장 먼 노드]  1. [가장 먼 노드]  1. [가장 먼 노드]  1. [가장 먼 노드]

노란색으로 표시된 2번 행 2번 열에서 k=2인 마법을 시전하게되면
각 방향마다 2칸씩, [그림2]와 같이 몬스터를 공격하게 되며
총 1. [가장 먼 노드] + 10 + 7 + 2 + 2 + 1. [가장 먼 노드]+ 1. [가장 먼 노드] = 26 마리를 처치하게 된다.

반면에 [그림3]와 같이 0번 행 2번 열에서 K=2인 마법을 시전하면 [그림4]와 같이
아래 대각선 방향 K칸에 해당되는 몬스터를 공격하게되며

총 7 + 2 + 0 + 7 = 16마리 몬스터를 처치할 수 있다.

마법사 Mort 씨가 마법을 한번 시전하여 처치할 수 있는 몬스터의 최대 수를 출력하시오.

첫번째 줄에 전투장의 가로세로크기인 N이 입력된다. (1. [가장 먼 노드]<= N <= 100)
다음 줄부터는 N줄에 걸쳐 각줄마다 N개의 정수가 공백으로 구분되어 입력된다. (0<= 정수 <= 100,000)
마지막 줄에는 마법의 시전범위 K가 입력된다. (1. [가장 먼 노드]<= K <= 100)

마법사가 잡을 수 있는 몬스터의 최대 수를 출력하시오.

'''
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())  # 가로세로크기 N
arr = [list(map(int,input().split())) for _ in range(N)]
K = int(input())  # 마법의 시전범위 K

dxy = [[1,1], [1,-1],[-1,-1], [-1,1]]
max_hap=0

for i in range(N):
    for j in range(N):
        hap = 0
        for dx,dy in dxy:
            for k in range(1,K+1):  # K만큼 순회하면서 값 더해줌
                nx = i + dx*k
                ny = j + dy*k

                if nx < 0 or nx >= N or ny <0 or ny >= N:
                    continue
                else:
                    hap += arr[nx][ny]
        if max_hap < hap:
            max_hap = hap
print(max_hap)