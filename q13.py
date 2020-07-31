for i in range(1, 11):
    for j in range(1, 11):
        multi = str(i * j)
        right_multi = multi.rjust(3)
        print(f'{right_multi}', end=' ')
    print(' ')
