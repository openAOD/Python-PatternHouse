size = int(input("Enter Number of Rows:  "))
for i in range(65, 65+size):
    for j in range(i, 65+size):
        a = chr(i)
        print(a, end="")
    print()