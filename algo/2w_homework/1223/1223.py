# SWEA 1223. [S/W 문제해결 기본] 6일차 - 계산기2

'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+56*+7+"

변환된 식을 계산하면 44를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.

'''
import sys
sys.stdin = open('input.txt', 'r')

oper = {'+': 0, '*': 1}  # 연산자 우선순위

def backward_notation(expr): # 후위표기하는 함수
    stack = []   # 연산자 담을 스택
    res = []   # 후위표기 담을 res

    for ch in expr:   # 하나씩 순회
        if ch.isdigit():   # 숫자형일때
            res.append(ch)
            continue
        if not stack or oper[stack[-1]] < oper[ch]:  # 빈 스택이거나 호출된 연산자의 우선순위가 높을 경우
            stack.append(ch)
        elif oper[stack[-1]] >= oper[ch]:  # 스택에 있는 마지막 요소와 호출된 연산자 우선순위 갖거나 작을 경우
            res.append(stack.pop())
            stack.append(ch)

    while stack:
        res.append((stack.pop()))  # 스택이 빌때까지 pop

    return ''.join(map(str,res))  #  34+56*7++

def calculation(expr):  # 후위표기 계산하는 함수
    stack = []  # 계산한 값 넣어 줄 stack

    for ch in backward_notation(expr):   # 후위표기법 순회
        if ch.isdigit():   # 문자열 숫자일 경우
            stack.append(ch)
            continue
        if ch == '*':  # 연산자 만났을 때 두번 팝 한 값을 다시 stack에 추가함
            val = oper[ch]  # 곱하기는 초기값 1로 설정 위함
            for _ in range(2):
                val *= int(stack.pop())
        else:
            val = oper[ch]   #  더하기는 val 초기값 0으로 설정 위함
            for _ in range(2):  # 두번 pop
                val += int(stack.pop())
        stack.append(val)  # 계산결과값 다시 stack에 추가


    return stack.pop()  # 순회 다 돌고 마지막에 담긴 것이 최종 결과 값

T = 10  # 테스트 케이스 수

for case in range(1, T+1):
    length = int(input())   # 문자열 길이
    expr = input()  # 표현식

    print(f'#{case} {calculation(expr)}')
