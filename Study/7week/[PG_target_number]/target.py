# 프로그래머스 [타겟 넘버]

from collections import deque

def solution(numbers, target):
    answer = 0
    idx = -1  # 인덱스
    hap = 0  # 합 값 담아줌

    queue = deque([(idx, hap)])

    while queue:
        i, v = queue.popleft()
        i += 1
        if i == len(numbers) and v ==target:
            answer += 1
        else:
            queue.append((i, v + numbers[i]))
            queue.append((i, v - numbers[i]))

    return answer

# print(solution([4,1,2,1], 4))






