size = int(input("Number of rows: "))

for i in range(size):
    for j in range(65+size-1,64,-1):
        print(chr(j), end=' ')
    print() 