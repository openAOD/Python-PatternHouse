n = 5
for i in range (n):
    for j in range (2*n,i,-1):
        print(' ', end='')
    for k in range (i+1):
        print('* ', end='')
    print()
for i in range (n):
    for j in range (n,i,-1):
        print(' ', end='')
    for k in range (i+1):
        print('* ', end='')
    for l in range (i+1, n):
        print(' ', end=' ')
    for m in range (i+1):
        print('* ', end='')
    print()
