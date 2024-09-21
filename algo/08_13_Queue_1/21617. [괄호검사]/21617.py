# SWEA. 21617 [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

'''
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.

예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.

정상적으로 짝을 이룬 경우 1. [가장 먼 노드], 그렇지 않으면 0을 출력한다.

print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1. [가장 먼 노드]≤T≤50

다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.


[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''
bracket = {"(" : ")", "{" : "}"}

def find_correct(exp):
    stack = []

    for ch in exp:
        if ch in bracket.keys():
            stack.append(ch)
        elif ch in bracket.values():
            if not stack or ch != bracket[stack[-1]]:
                return False
            stack.pop()
    return not stack   # 빈 스택이면 True 반환

T = int(input())

for case in range(1, T+1):
    exp = input()

    print(f'#{case}' ,end =' ')
    if find_correct(exp):
        print(1)
    else:
        print(0)