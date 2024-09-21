# import sys
# sys.stdin = open('input.txt', 'r')
#
for case in range(1, 11):
    length = int(input())
    arr = [list(map(int,input().split())) for _ in range(length)]  # 100X100 배열 입력

    max_deadlock = 0
    for col in range(length):   # 열 순서대로 배열 순회
        find = False
        for row in range(length):
            if arr[row][col] == 1:   # '순서가 1. [가장 먼 노드],2 이렇게 되면 교착상태 1. [가장 먼 노드] 1. [가장 먼 노드] 2 도 가능'  처음 1. [가장 먼 노드] 끝 2면 교착상태 1개로 판단
                find = True
            if arr[row][col] == 2:   # 1을 찾고 그다음 2가 나오면 find로 인해 그 교착상태임을 확인 가능
                if find:
                    max_deadlock+=1    # 교착 합 갱신
                    find = False  # 그러고나서 다시 처음부터 찾아야하니 find False로 돌려줌

    print(f'#{case} {max_deadlock}')


# import sys
# sys.stdin = open('input.txt', 'r')
#
for case in range(1, 11):
    length = int(input())
    arr = [list(input().split()) for _ in range(length)]  # 100X100 배열 입력
    deadlock = 0   # 교착 갯수 담아줄 변수 초기값 설정

    for col in range(length):  # 열방향으로 row 순회
        str = ''
        for row in range(length):
            if arr[row][col] !='0':   # 0을 제외한 숫자를 string을 들고옴
                str += arr[row][col]   # 예 ) 1번째 열 : '1. [가장 먼 노드]' / 3번째 열 : '2121'

        deadlock += str.count('12')   # '12' 순이면 교착 상태임을 알 수 있음 /   '112'이어도 교차 상태는 1개임
                                        # 각 열 순회하면서 12순이면 교착상태이니 카운트해줌
    print(f'#{case} {deadlock}')


