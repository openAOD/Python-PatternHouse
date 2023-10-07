n = 4
for i in range(n+1):
    for j in range(0,i):
        print(n-j-1, end = " ")
    print()
for i in range(n-1, 0, -1):
    for j in range(0,i):
        print(n-j-1, end = " ")
    print()
