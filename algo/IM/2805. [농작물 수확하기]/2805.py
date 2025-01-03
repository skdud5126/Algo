# SWEA. 2805. [농작물 수확하기] 농작물 수확하기


'''
N X N크기의 농장이 있다.

이 농장에는 이상한 규칙이 있다.

규칙은 다음과 같다.


   ① 농장은 크기는 항상 홀수이다. (1. [가장 먼 노드] X 1. [가장 먼 노드], 3 X 3 … 49 X 49)

   ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.




1. [가장 먼 노드] X 1크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 3이다.

3 X 3크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 16 (3 + 2 + 5 + 4 + 2)이다.

5 X 5크기의 농장에서 자라는 농작물의 수확하여 얻을 수 있는 수익은 25 (3 + 2 + 1. [가장 먼 노드] + 1. [가장 먼 노드] + 2 + 5 + 1. [가장 먼 노드] + 1. [가장 먼 노드] + 3 + 3 + 2 + 1. [가장 먼 노드])이다.

농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.


[제약 사항]

농장의 크기 N은 1. [가장 먼 노드] 이상 49 이하의 홀수이다. (1. [가장 먼 노드] ≤ N ≤ 49)

농작물의 가치는 0~5이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 공백으로 농장의 규칙에 따라 얻을 수 있는 수익을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


'''
T = int(input())  # 테스트 케이스 T

for case in range(1, T+1):
    N = int(input())  # 농장 크기 N
    arr = [list(map(int, input())) for _ in range(N)]   # 문제에 공백없이 입력되어있는 점 주의!

    hap = 0   # 농작물 합 초기값 설정
    for i in range(N):
        if i <= (N // 2):   # N이 5라고 가정했을 때 5//2 2보다 작은 인덱스 범위 값들 가져옴
            for j in range(N//2-i, N//2+i+1):
                hap += arr[i][j]
        else:
            for j in range(i-N//2, N-(i-N//2)):   # 중반부 넘었을때의 인덱서 범위 지정
                hap += arr[i][j]
    print(f'#{case} {hap}')