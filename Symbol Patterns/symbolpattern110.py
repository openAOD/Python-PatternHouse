n=5
for i in range(n):
    for j in range (1,n-i):
        print('*', end='')
    for k in range (i,2*i+1):
        print(k+1, end='')
        if k+1 == 2*i+1:
            for a in range (k, i, -1):
                print(a, end='')
            break
    for l in range (n-i, 1, -1):
        print('*', end='')
    print()
