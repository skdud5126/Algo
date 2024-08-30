def make_tree(node):
    global num

    if node <= N:
        make_tree(node*2)
        tree[node] = num
        num+=1
        make_tree(node*2+1)

T = int(input())

for case in range(1, T+1):
    N = int(input())
    node=1
    num = 1
    tree = [0]*(N+1)

    make_tree(node)  # [0, 4, 2, 6, 1, 3, 5]

    print(f'#{case} {tree[1]} {tree[N//2]}')
