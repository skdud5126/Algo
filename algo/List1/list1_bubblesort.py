N = 6
arr = [7, 2, 5, 3, 4, 1]

for i in range(N-1, 0, -1): # 각 구간의 끝 인덱스 i
    for j in range(i): # 각 구간의 두 개씩 비교할 때 왼쪽 원소의 인덱스 j
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j] # 왼쪽 원소가 더 크면 교환

print(*arr)