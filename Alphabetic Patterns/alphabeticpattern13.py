size = int(input("Enter Number of Rows:  "))
for i in range(0, size):
    for j in range(65 + i, 64, -1):
        a = chr(j)
        print(a, end="")
    print()