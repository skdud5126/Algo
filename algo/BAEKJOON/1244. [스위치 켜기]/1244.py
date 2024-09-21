# BAEKJOON. 1244 스위치 켜고 끄기

swap = {'1. [가장 먼 노드]' : '0', '0': '1. [가장 먼 노드]'}

switch = int(input())  #  스위치 갯수
sw_li= list(input().split())   # 스위치 상태
students = int(input())  # 학생 수


for _ in range(students):
    jender, num = map(int, input().split())  # 성별, 학생이 받은 수

    if jender == 1:   # 남자일 때
        for i in range(switch):   # 스위치 갯수
            if (i+1) % num == 0:   # num 의 배수일때 스위치 전환
                sw_li[i] = swap[sw_li[i]]

    elif jender == 2:  # 여자일 때
        idx = 1
        if num - 1 - idx >= 0 and num - 1 + idx < switch:   #  인덱스 범위 지정
            while sw_li[num-1-idx] == sw_li[num-1+idx]:   # 좌우 스위치 상태 같으면
                sw_li[num - 1 - idx], sw_li[num - 1 + idx] = swap[sw_li[num - 1 - idx]], swap[sw_li[num - 1 + idx]]
                idx += 1
                if num - 1 - idx < 0 or num - 1 + idx >= switch:
                    break
        sw_li[num-1] = swap[sw_li[num-1]]

for i in range(len(sw_li)):   # 스위치 20개씩 출력해줌
    if ((i+1)%20) == 0:
        print(sw_li[i], end = ' ')
        print()
    else:
        print(sw_li[i], end = ' ')

