Data = [0, 4, 1, 3, 1, 2, 4, 1]
Counts = [0] * 5      # Data가 0~4 까지의 정수

N = len(Data)    # Data의 크기
Temp = [0] * N   # 정렬된 결과 저장

# 1단계 : Data 원소 별 개수 세기
for x in Data:   # Data의 원소 x를 가져와서 Counts[x]에 개수 기록
    Counts[x] += 1


# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1, 5):        # Count[1. [가장 먼 노드]] ~ Count[4] 까지 누적개수
    Counts[i] = Counts[i-1] + Counts[i]


# 3단계 : Data의 맨 뒤부터 Temp에 자리 잡기
for i in range(N-1, -1, -1):
    Counts[Data[i]] -= 1   # 누적개수 1개 감소
    Temp[Counts[Data[i]]] = Data[i]

print(Temp)