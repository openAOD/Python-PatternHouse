n = 7
a = n//2+1
for i in range (a):
    for j in range (i+1):
        if j==i or j==0:
            print(' *', end=' ')
        else:
            print('  ', end=' ')
    print()
for i in range (n-a, 0, -1):
    for j in range (i):
        if j == 0 or j == i-1:
            print(' *', end=' ')
        else:
            print('  ', end=' ')
    print()
