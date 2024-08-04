# 부분집합 합 구하기

#arr = [3, 6, 7, 1, 5, 4]
arr= [1,2,3]
n = len(arr)   # n : 원소의 개수

for i in range(1<<n):   # 1<<n : 부분 집합의 개수
    for j in range(n):   # 원소의 수만큼 비트를 비교함
        if i & (1<<j):   # i의 j번 비트가 1인 경우
            print(arr[j], end = ',')   # j번 원소 출력
    print()
print()


# swea List2 - 연습문제2. 부분집합 합 문제 구현하기

# for case in range(1, int(input())+1):
#     arr = list(map(int, input().split()))
#     count = 0
#     for i in range(1,1<<len(arr)):  # 모든 부분 집합 조합 수
#         subset = []
#         for j in range(len(arr)):
#             if i & (1<<j):
#                 subset.append(arr[j])
#         hap = sum(subset)
#
#         if hap == 0:
#             count+=1
#     if count == 0:
#         print(f'#{case} 0')
#     else:
#         print(f'#{case} 1')

T = int(input())

for case in range(1, T+1):
    arr = list(map(int, input().split()))   # 배열 전달받음
    li = []
    for i in range(1,1<<len(arr)):   # 공집합 제외 모든 부분집합 생성 수
        subset = []
        for j in range(len(arr)):
            if i & (1<<j):
                subset.append(arr[j])
        hap = sum(subset)
        li.append(hap)
    if 0 in li:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')