size = int(input("Enter Number of Rows:  "))
for i in range(65+size -1, 64, -1):
    for j in range(64, i):
        a = chr(i)
        print(a, end="")
    print()