n = 4
for i in range (n):
    for j in range (i, n-1):
        print(' ', end='')
    for k in range (2*i+1):
        print('*', end='')
    for l in range (i+1, n):
        print(' ', end=' ')
    for m in range (2*i+1):
        print('*', end='')
    print()
