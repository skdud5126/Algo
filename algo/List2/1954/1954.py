for i in range(3):  # 0 1 2
    for j in range(3):  # 0 1 2
        if i%2 == 0:

            print(i,j)
        else:
            if j == 3:
                j = i
            print(j,i)