n = 5
for i in range (n):
    j = -1
    for j in range (n-i-1):
        print(' ', end='')
    for k in range (2*i+1) :
        if (j+k)%2 != 0:
            print('*', end='')
        else:
            print('#', end='')
    print()
