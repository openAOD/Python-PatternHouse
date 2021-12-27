n = int(input())
for i in range (n):
    for j in range (1,n+1-i):
        print(j, end='')
    for k in range (2*i+1):
        print('*' ,end='')
    for l in range (n-i,0,-1):
        print(l, end='')
    print()
for m in range (2*n+1):
    print('*', end='')
