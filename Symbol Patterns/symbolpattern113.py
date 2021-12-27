n = 5
for i in range (n):
    j = -1
    for j in range (n-i-1):
        print(' ', end='')
    for k in range (i+1) :
        print('(', end='')
    print('*', end='')
    for l in range (i+1):
        print(')', end='')
    print()
