
operator = {'*' : 1, '/' : 1, '+': 0, '-': 0}   # 연산자 우선순위 지정


T = int(input())  # 테스트 케이스 수 T

for case in range(1, T+1):
    expression = input()   # 수식 입력 받음
    stack = []    # 연산자 담을 빈 스택
    res = []  # 후위표기 담을 리스트

    for char in expression:  # 한개씩 꺼내옴
        if char.isdigit():   # 숫자일때 res에 추가
            res.append(char)
        else:  # 숫자가 아닐 때
            if not stack or operator[stack[-1]] < operator[char]:   # stack이 비었거나 스택에 담겨있는 연산자보다 호출된 우선순위가 클 경우 스택에 추가함
                stack.append(char)  # 스택에 담아줌
            else:   # 호출된 연산자 우선순위가 스택에 있는 것보다 우선순위가 같거나 작을때 pop해줌
                res.append(stack.pop())   # res에 stack pop 더해줌
                stack.append(char)   # 스택에 호출된 연산자 더해줌

    while stack:   # 스택에 남아있는 연산자 없어질때까지 pop
        res.append(stack.pop())
    print(f'#{case} {"".join(map(str,res))}')
