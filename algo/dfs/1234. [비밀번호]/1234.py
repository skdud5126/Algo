# 1234. [비밀번호]

def delete_repeat(password):
    stack = []

    for num in password:
        if not stack or stack[-1]!= num:
            stack.append(num)
        else:
            stack.pop()
    return stack

for case in range(1, 11):
    N, password = input().split()
    res = delete_repeat(password)
    print(f'#{case} {"".join(res)}')
