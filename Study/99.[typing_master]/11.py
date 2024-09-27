import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')
from itertools import permutations

N = int(input())    # N : 팀 개수
S, P = map(int, input().split())    # S : 강사님 점수, P : 강사님 정확도
student_score = [list(input().split()) for _ in range(2*N)]   # 학생 점수
print(student_score)


# 강사님 점수
t_score = int(S * (P/100))
# 강사님 점수 자릿수
t_score_len = len(str(t_score))

# 개인 점수 구하기
score_lst = []
for lst in student_score:
    # 타자 속도 * 정확도
    score = int(lst[0]) * (int(lst[1])/100)
    # 만약 한글로 했으면 0.7 곱해주기
    if lst[2] == 'K':
        score *= 0.7
    score_lst.append(int(score))

# 팀 별 평균 점수 구하기
# 원점수
current_score = [0] # 0번째 안씀
team_score = {}
# 강사님 점수와의 점수 차이
diff = []

for i in range(N):
    # 팀장과 팀원의 점수 평균
    current_score.append(int((score_lst[2 * i] + score_lst[2 * i + 1])/2))
    team_score[i + 1] = str(current_score[i + 1]).zfill(t_score_len)

    split_score = list(team_score[i + 1])

    # 순열 구하기
    nPr = list(permutations(split_score, 3))
    min_diff = 1000

    # 강사님 점수와 가장 적은 점수 차이 구하기
    for num in nPr:
        case = 0
        for j in range(3):
            case += int(num[j])*(10**j)
        if abs(t_score - case) < min_diff:
            min_diff = abs(t_score - case)

    # 각 팀별 최소 점수 차이를 리스트에 저장
    diff.append([i +1, min_diff])    # [[1, 333], [2, 8], [3, 56], [4, 69], [5, 46], [6, 91], [7, 159], [8, 0]]



diff = sorted(diff, key=lambda x:x[1])   # [[8, 0], [2, 8], [5, 46], [3, 56], [4, 69], [6, 91], [7, 159], [1, 333]]
print(diff)
print(current_score)  # [0, 635, 635, 525, 554, 635, 554, 554, 525]

# 점수차 같은 경우 원점수 비교하여 정렬
for i in range(N - 1):
    for j in range(i + 1, N):
        if diff[i][1] != diff[j][1]: continue
        if current_score[diff[i][0]] < current_score[diff[j][0]]:
            diff[i], diff[j] = diff[j], diff[i]

# 원점수 비교 : [[1, 8], [2, 8], [5, 8], [4, 89], [6, 89], [7, 89], [3, 91], [8, 91]]

# 원점수 같을 경우 제출순위 비교하여 정렬




for i in range(N):
    print(f'{i + 1}등: {student_score[(diff[i][0] - 1) * 2][-1]} {student_score[(diff[i][0] - 1) * 2 + 1][-1]} ({diff[i][0]} 팀)'
          f' | 점수 차 : {diff[i][1]} | 원점수: {current_score[diff[i][0]]} | 제출순위 : ')