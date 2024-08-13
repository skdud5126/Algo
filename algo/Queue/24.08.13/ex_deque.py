from collections import deque
deque_q = deque()

list_q = []
for i in range(1000000):
    list_q.append(i)
for _ in range(1000):
    list_q.pop(0)
print('end')