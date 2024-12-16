# BackJoon 1316.[그룹 단어 체커]

'''
[문제]

그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.

예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

[입력]

첫째 줄에 단어의 개수 N이 들어온다.

N은 100보다 작거나 같은 자연수이다.

둘째 줄부터 N개의 줄에 단어가 들어온다.

단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

[출력]

첫째 줄에 그룹 단어의 개수를 출력한다.

'''

N = int(input())  # 단어의 갯수 N
cnt = 0  # 그룹 단어의 개수

for _ in range(N):
    word = input()  # 단어 입력
    stack = []  # 스택을 이용해 연속된 문자를 추적
    isGroup = True  # 그룹 단어 여부를 나타내는 플래그

    for i in range(len(word)):
        # 첫 번째 문자가 스택에 없거나, 스택의 마지막 문자와 다르면
        if not stack or word[i] != stack[-1]:
            stack.append(word[i])  # 스택에 문자 추가
        elif word[i] == stack[-1]:
            # 중간에 떨어져서 같은 문자가 나타나면 그룹 단어가 아님
            continue

        # 문자가 스택에 이미 존재하면 그룹 단어 아님
        if word[i] in stack[:-1]:
            isGroup = False
            break

    if isGroup:
        cnt += 1  # 그룹 단어이면 카운트 증가

print(cnt)

