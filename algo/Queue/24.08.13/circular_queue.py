N = 4
cQ = [0] * N
front = rear = 0

rear = (rear + 1) % N  # enq(1)
cQ[rear] = 1

rear = (rear + 1) % N  # enq(2)
cQ[rear] = 2

rear = (rear + 1) % N  # enq(3)
cQ[rear] = 3

front = (front + 1) % N
print(cQ[front])