row = int(input("Enter number of rows : "))
for i in range(1, row+1):
    for j in range(65, 65+i):
        print(chr(j), end=' ')
    print()