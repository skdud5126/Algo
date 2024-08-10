# SWEA. 1222 [S/W 문제해결 기본] 6일차 - 계산기1

'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5+6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+5+6+7+"

변환된 식을 계산하면 25를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 + 하나뿐이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 문자열 계산식의 길이가 주어진다. 그 다음 줄에 문자열 계산식이 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.

'''
import sys
sys.stdin = open('input.txt','r')

def backward_notation(expr):      # 후위표기 나타내는 함수(backword_notation)
    stack = []  # 연산자 담아줄 stack
    res = []   # 후위표기법 표현 담아줄 res

    for ch in expr:   # 표현식 하나씩 순회
        if ch.isdigit():   # 하나씩 뽑은 문자열이 숫자형이면
            res.append(ch)
            continue   # 아니면 이어서 순회
        if not stack:   # 연산자를 만났을 때 빈 스택
            stack.append(ch)
        elif stack[-1] == ch:   # 스택에 +가 있으면 기존에 있던 연산자 pop해서 res에 추가해주고 호출된 연산자 스택에 담기
            res.append(stack.pop())
            stack.append(ch)
    while stack:   # 순회 돌았을때 스택에 남아있을 경우 스택이 빌때까지 pop해서 res에 붙여줌
        res.append(stack.pop())

    return ''.join(map(str,res))

def calculation(expr):
    stack = []

    for ch in backward_notation(expr):   # 후위표기법으로 받은 것 순회   34+5+6+7+8+
        if ch.isdigit():  # 숫자형일경우
            stack.append(ch)
            continue
        val = 0
        for _ in range(2):  # 연산자 만나면 스택에 있는 2번 pop하여 더해줌
            val += int(stack.pop())  # int 형변환
        stack.append(val)   # 계산결과 다시 스택에 추가해줌
    return stack[-1]   # 마지막 스택에 남은 것이 계산 결과 반환해줌


T = 10   # 테스트 케이스 수

for case in range(1, T+1):
    length = int(input())  # 문자열 길이 N
    expr = input()   # 문자열 계산식

    print(f'#{case} {calculation(expr)}')