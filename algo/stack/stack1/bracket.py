def check_match(expression):

    stack = []
    matching_dict = {'(':')', '[':']', '{':'}'}

    for char in expression:
        if char in matching_dict.keys():
            stack.append(char)    # 열린괄호 만나면 스택에 추가해줌
        elif char in matching_dict.values():
            if not stack or char != matching_dict[stack[-1]]: # 스택에 아무거나 없거나 닫힌괄호가 같지 않았을 경우 False 반환.
                return False
            stack.pop()  # 짝이 맞을 경우 pop
    return not stack  # 모든 문자를 순회한 후 스택이 비어 있으면 True 반환, 그렇지 않으면 False 반환


example = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)"]


for ex in example:
    if check_match(ex):
        print(f'{ex}는 올바른 괄호')
    else:
        print(f'{ex}는 잘못된 괄호')