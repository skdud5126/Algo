# SWEA. 1983 조교의 성적 매기기

import sys
sys.stdin = open('input.txt', 'r')

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input()) # 테스트 케이스 수

for case in range(1, T+1):
    N, K = map(int, input().split())  # N 학생수 / K 번째 학생의 성적 알고 싶음
    score = [list(map(int,input().split())) for _ in range(N)]   # 학생 성적 배열
    same_score = N//10  # 학생 수에 따라 같은 성적을 줄 학생 수
    res = []

    for idx, value in enumerate(score, start = 1):  # 인덱스 번호(1부터 시작 지정)와 값을 가져옴
        res.append([value[0]*0.35 + value[1]*0.45 + value[2]*0.2, idx])   #  [[74.6, 1], [92.55000000000001, 2], [88.8, 3], [99.45, 4], [72.35, 5], [85.85000000000001, 6], [96.25, 7], [68.95, 8], [85.5, 9], [85.75, 10]]

    res.sort(reverse= True)  # 성적 순으로 정렬(idx번호기준 아님)

    for i in range(N):
        res[i].append(grades[i//same_score])

    for student_grade in res:
        if student_grade[-2] == K:   # 처음 학생들의 위치 [74,6, 1, 'C0']
            print(f'#{case} {student_grade[-1]}')   # 요소 마지막이 학점 표시
            break


