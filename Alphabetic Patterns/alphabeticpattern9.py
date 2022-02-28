n = int(input("Number of rows: "))

for i in range(65, 65+n):
    for j in range(64, i):
        a = chr(i)
        print(a, end="")
    print() 