# SWEA. 1210 Ladder1

'''
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨) 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.

X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.

[제약 사항]

한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.

[입력]

입력 파일의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도착하게 되는 출발점의 x좌표를 출력한다.

'''


import sys
sys.stdin = open('input.txt', 'r')


def correct_ladder(x,y):
    dxy = [[1, 0], [0,-1], [0, 1]]  # 사다리는 방향 순서 중요! 하, 좌, 우 순서로 좌표 지정
    visited_box = [[0]*size for _ in range(size)]   # 방문한 곳 표시하기 위한 0인 100X100 배열 생성

    visited_box[x][y] = 1   # 시작지점 표시

    while x != 99:  # 행이 99번까지 도달해야하기에 반복문 실행

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= size or ny < 0 or ny >= size: # 방향범위 넘어난 곳 제한
                    continue
            if not input_ladder[nx][ny]:  # 사다리가 아닌 경우 (0)
                    continue

            if visited_box[nx][ny]:   # 이미 방문한 곳이면 패스
                     continue

            visited_box[nx][ny] = 1

            x, y = nx , ny  # 이동한 좌표 다시 재할당

    if input_ladder[x][y] == 2:  # while 빠져나와 2를 만나면 True 반환
        return True
    return False


size = 100
for _ in range(1, 11):   # 10개의 테스트 케이스 주어짐
    case = int(input())   # 케이스 순번 입력 받음
    input_ladder = [ (list(map(int,input().split()))) for _ in range(size)]  # 100x100 이중배열 입력 받음

    result = -1

    for y in range(size):   # 모든 원소 접근
        if input_ladder[0][y] == 0:   # 열에 있는 숫자가 1일때만 출발 Early return 사용
            continue


        if correct_ladder(0,y):    # 2에 도착한 열의 번호 반환하기 위함
            result = y
            break    # 값이 나왔으므로 포문 탈출

    print(f'#{case} {result}')
