# SWEA. 21675 [파이썬 S/W 문제해결 기본] 5일차 - Forth

'''
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다.

예를 들어 3+4는 다음과 같이 표기한다.

3 4 + .

Forth에서는 동작은 다음과 같다.

숫자는 스택에 넣는다.

연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

‘.’은 스택에서 숫자를 꺼내 출력한다.

Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오.

만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.


다음은 Forth 연산의 예이다.

코드         출력

4 2 / .      2

4 3 - .      1. [가장 먼 노드]

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1. [가장 먼 노드]≤T≤50

다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.

나눗셈의 경우 항상 나누어 떨어진다.


[출력]

#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
'''



T = int(input())  # 테스트 케이스 T

for case in range(1, T+1):
    expr = list(input().split())   # 표현식
    stack = []    # 피연산자들 담을 빈 스택 리스트
    val = []   # 팝해서 넣을 값들

    for char in expr:
        if char.isdigit():   # 숫자형일때
            stack.append(char)   # 스택에 추가해줌
            continue

        if char != '.':  # .을 제외하고 연산자 만났을 때 계산 수행한다.
            if not stack or len(stack) < 2:  # 숫자형이 아닐 때 /스택에 없는 상태에서 연산자 만나면 error/ 스택에 길이가 1개인데 연산자 만나면 연산 불가능
                print(f'#{case} error')
                break
            for _ in range(2):  # stack에 있던 값 꺼내오기 두 번 반복
                val.append(int(stack.pop()))  # 숫자로 있는거 int로 받아옴
            res = 0   # 연산작업 값 담아 줄 변수 초기값 설정
            if char == '+':
                res = val[-1] + val[-2]
            if char == '-':
                res = val[-1] - val[-2]
            if char == '*':
                res = val[-1] * val[-2]
            if char == '/':
                res = val[-1] // val[-2]
            stack.append(res)    # 연산 결과값 다시 stack에 추가
        else:
            if len(stack) == 1:  # '.' 만났을때 스택안에 있는게 정답임 하나만 존재해야하므로 예외처리 구문
                print(f'#{case} {stack.pop()}')
            else:
                print(f'#{case} error')
