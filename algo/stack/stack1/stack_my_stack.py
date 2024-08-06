stack_size = 10

stack = [0] * stack_size
top = -1

# push 1, 2, 3

top += 1   # push(1)
stack[top] = 1

top += 1
stack[top] = 2

top += 1
stack[top] = 3

top -= 1  # pop()
print(stack[top+1])
print(stack[top])
top -= 1
print(stack[top])
top -= 1
