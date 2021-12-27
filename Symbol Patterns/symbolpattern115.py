n = 5
for i in range (n):
    for j in range (n,i,-1):
        print(' ', end=' ')
    for k in range(i+1):
        if k == 0 or i == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for m in range (i):
        if m == i-1 or i == n-1:
            print('*', end=' ')
            continue
        print(' ', end=' ')
    print()
