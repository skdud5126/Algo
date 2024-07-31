arr1 = [0] * 3

arr2 = [[0] * 3 for _ in range(2)]   # 2행 빈 배열 생성
print(arr1)
print(*arr1)

for i in range(2):
    print(*arr2[i])

for i in range(2):
    for j in range(3):
        print(arr2[i][j], end = ' ')
    print()


arr = [[1, 2, 3], [4, 5, 6]]
print(len(arr))
print(len(arr[0]))

# 각 행의 합 중 최댓값 구하기
max_value = 0
for i in range(2):
    hap = 0
    for j in range(3):
        hap += arr[i][j]
    if max_value < hap:
        max_value = hap
print(max_value)

# 각 열의 합 중 최소값 구학

min_value = 0
for j in range(3):
    hap = 0
    for i in range(2):
        hap += arr[j][i]
    if min_value 
# 안좋은 예시

arr= [[0]*3]*2