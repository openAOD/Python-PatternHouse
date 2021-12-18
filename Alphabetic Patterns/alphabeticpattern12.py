size = int(input("Enter Number of Rows:  "))
for i in range(65+size, 64, -1):
    for j in range(65+size, i, -1):
        a = chr(i)
        print(a, end="")
    print()